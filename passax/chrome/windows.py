import base64
import getpass
import json
import os
import platform
from pathlib import Path
from typing import Union

import win32crypt
from Crypto.Cipher import AES

from passax.chrome.base import ChromeBase
from passax.exceptions import *


class ChromeWindows(ChromeBase):
    def __init__(self, browser: str = "chrome", verbose: bool = False):
        """
        Decryption class for Windows 10.
        Notice that older versions of Windows haven't been tried yet.
        The code will probably not work as expected.
        :param browser: Choose which browser use. Available: "chrome" (default), "opera", and "brave".
        :param verbose: print output
        """

        super(ChromeWindows, self).__init__(verbose)

        if platform.system() != "Windows":
            raise BadOS("Use your system's OS")

        if not browser.lower() in self.available_browsers:
            raise BrowserNotImplemented

        self.username = getpass.getuser()
        self.browser = browser.lower()

        self._browser_paths = []
        self._database_paths = []
        self.keys = []

        base_path = r"C:\Users\{}\AppData".format(getpass.getuser())

        self.browsers_paths = {
            "chrome": os.path.join(base_path, r"Local\Google\{chrome}\User Data\Local State"),
            "opera": os.path.join(base_path, r"Roaming\Opera Software\Opera Stable\Local State"),
            "brave": os.path.join(base_path, r"Local\BraveSoftware\Brave-Browser\User Data\Local State")
        }

        self.browsers_database_paths = {
            "chrome": os.path.join(base_path, r"Local\Google\{chrome}\User Data\Default\Login Data"),
            "opera": os.path.join(base_path, r"Roaming\Opera Software\Opera Stable\Login Data"),
            "brave": os.path.join(base_path, r"Local\BraveSoftware\Brave-Browser\User Data\Default\Login Data")
        }

    def get_windows(self):
        """Return database paths and keys for Windows
        """

        if self.browser == "chrome":
            chrome_versions = ['chrome', 'chrome dev', 'chrome beta', 'chrome canary']

            # Fetch all Chrome versions paths
            self._browser_paths = [
                self.browsers_paths["chrome"].format(chrome=ver)
                for ver in chrome_versions if
                os.path.exists(self.browsers_paths["chrome"].format(chrome=ver))]

            # Fetch all database paths
            self._database_paths = [
                self.browsers_database_paths["chrome"].format(chrome=ver)
                for ver in chrome_versions if
                os.path.exists(self.browsers_paths["chrome"].format(chrome=ver))]

        else:
            self._browser_paths = [self.browsers_paths[self.browser]]
            self._database_paths = [self.browsers_database_paths[self.browser]]

        # Get the AES key
        self.keys = [self.__class__.get_encryption_key(path) for path in self.browser_paths]
        return self.database_paths, self.keys

    @staticmethod
    def decrypt_windows_password(password, key) -> str:
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

        except:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])

            except Exception:
                # Not handled error. Abort execution
                raise NotImplemented

    @property
    def browser_paths(self):
        return self._browser_paths

    @property
    def database_paths(self):
        return self._database_paths

    @staticmethod
    def get_encryption_key(path: Union[Path, str]):
        """Return the encryptation key of a path
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
