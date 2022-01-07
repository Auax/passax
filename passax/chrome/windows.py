import base64
import getpass
import json
import os
import platform
from pathlib import Path
from typing import Union, Type

import win32crypt
from Crypto.Cipher import AES

from passax.browser_version import BrowserVersion
from passax.chrome import browsers
from passax.chrome.base import ChromeBase
from passax.exceptions import *


class Chrome(ChromeBase):
    def __init__(self,
                 browser: Type[BrowserVersion] = browsers.Chrome,
                 verbose: bool = False,
                 blank_passwords: bool = False):
        """
        Decryption class for Windows 10.
        Notice that older versions of Windows haven't been tried yet.
        The code will probably not work as expected.
        :param browser: Choose which browser use.
        :param verbose: print output
        :param blank_passwords: save or not blank passwords
        """

        super(Chrome, self).__init__(verbose, blank_passwords)

        if platform.system() != "Windows":
            raise BadOS("Use a Windows system for this class.")

        self.browser = browser()
        if not isinstance(self.browser, BrowserVersion):
            raise BrowserNotImplemented

        # This is where all the paths for the installed browsers will be saved
        self._browser_paths = []
        self._database_paths = []

        self.keys = []
        base_path = r"C:\Users\{}\AppData".format(getpass.getuser())

        self.browsers_paths = {
            "chrome": os.path.join(base_path, r"Local\Google\{ver}\User Data\Local State"),
            "opera": os.path.join(base_path, r"Roaming\Opera Software\{ver}\Local State"),
            "brave": os.path.join(base_path, r"Local\BraveSoftware\{ver}\User Data\Local State")
        }
        self.browsers_database_paths = {
            "chrome": os.path.join(base_path, r"Local\Google\{ver}\User Data\Default\Login Data"),
            "opera": os.path.join(base_path, r"Roaming\Opera Software\{ver}\Login Data"),
            "brave": os.path.join(base_path, r"Local\BraveSoftware\{ver}\User Data\Default\Login Data")
        }

    @property
    def browser_paths(self):
        return self._browser_paths

    @property
    def database_paths(self):
        return self._database_paths

    @ChromeBase.get
    def fetch(self):
        """
        Return database paths and keys for Windows
        """
        # Get the AES key
        self.keys = [self.__class__.get_encryption_key(path) for path in self.browser_paths]
        return self.database_paths, self.keys

    @staticmethod
    def get_encryption_key(path: Union[Path, str]):
        """
        Return the encryption key of a path
        """
        try:
            with open(path, "r", encoding="utf-8") as file:  # Open the "Local State"
                local_state = file.read()
                local_state = json.loads(local_state)

        except FileNotFoundError:
            raise FileNotFoundError("Cannot find Local State file.")

        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]  # Remove "DPAPI" string at the beginning
        # Return the decrypted key that was originally encrypted
        # using a session key derived from current user's login credentials
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    @staticmethod
    def decrypt_windows_password(password: bytes, key: bytes) -> str:
        """
        Input an encrypted password and return a decrypted one.
        """
        try:
            # Get the initialization vector
            iv = password[3:15]
            password = password[15:]
            # Generate cipher
            cipher = AES.new(key, AES.MODE_GCM, iv)
            # Decrypt password
            return cipher.decrypt(password)[:-16].decode()

        except Exception:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])

            except Exception:
                # Not handled error. Abort execution
                raise NotImplemented
