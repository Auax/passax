import os
import platform
import re
import subprocess

from Crypto.Hash import SHA1
from Crypto.Protocol.KDF import PBKDF2

from passax.chrome.base import ChromeBase
from passax.exceptions import *


class ChromeMacOS(ChromeBase):
    """ Decryption class for Chrome in MacOS """

    def __init__(self, browser: str = "chrome", verbose: bool = False, blank_passwords: bool = False):
        """
        Decryption class for MacOS. Only tested in the macOS Monterrey version.
        :param browser: Choose which browser use. Available: "chrome" (default), "opera", and "brave".
        :param verbose: print output
        """

        super(ChromeMacOS, self).__init__(verbose, blank_passwords)

        if platform.system() != "Darwin":
            raise BadOS("Use your system's OS")

        if not browser.lower() in self.available_browsers:
            raise BrowserNotImplemented

        self.keys = []
        self._browser_paths = []
        self._database_paths = []

        self.browser = browser.lower()
        self.browsers_paths = {
            "chrome": os.path.expanduser("~/Library/Application Support/Google/{chrome}/Default"),
            "brave": os.path.expanduser("~/Library/Application Support/BraveSoftware/Brave-Browser/Default")
        }

        self.browsers_database_paths = {
            "chrome": os.path.expanduser("~/Library/Application Support/Google/{chrome}/Default/Login Data"),
            "brave": os.path.expanduser("~/Library/Application Support/BraveSoftware/Brave-Browser/Default/Login Data")
        }

    @property
    def browser_paths(self):
        return self._browser_paths

    @property
    def database_paths(self):
        return self._database_paths

    @ChromeBase.get
    def get_macos(self):
        """
        Return database paths and keys for MacOS
        """

        # The system will notify the user and ask for permission
        # even running as a sudo user as it's trying to access the keychain.

        safe_storage_key = None

        if self.browser == "chrome":
            for ver in ChromeBase.google_chrome_versions:
                for j in self._browser_paths:
                    if ver in j:
                        safe_storage_key = subprocess.check_output(
                            f"security 2>&1 > /dev/null find-generic-password -ga '{ver.capitalize()}'", shell=True)
                        safe_storage_key = re.findall(r'\"(.*?)\"', safe_storage_key.decode("utf-8"))[0]

        else:
            safe_storage_key = subprocess.check_output(
                f"security 2>&1 > /dev/null find-generic-password -ga '{self.browser.capitalize()}'", shell=True)
            safe_storage_key = re.findall(r'\"(.*?)\"', safe_storage_key.decode("utf-8"))[0]

        if not safe_storage_key:
            raise MacOSKeychainAccessError("Error retrieving the password in the keychain.")

        # Decrypt the keychain key to a hex key
        self.keys.append(PBKDF2(safe_storage_key, b'saltysalt', 16, 1003, hmac_hash_module=SHA1))

        return self.database_paths, self.keys
