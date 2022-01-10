import os
import platform
import re
import subprocess
from typing import Type, Union

from Crypto.Hash import SHA1
from Crypto.Protocol.KDF import PBKDF2

from passax.browser_version import BrowserVersion
from passax.chrome import browsers
from passax.chrome.base import ChromeBase
from passax.exceptions import *


class Chrome(ChromeBase):
    """ Decryption class for Chrome in MacOS """

    def __init__(self,
                 browser: Type[BrowserVersion] = browsers.Chrome,
                 verbose: bool = False,
                 blank_passwords: bool = False):
        """
        Decryption class for MacOS. Only tested in the macOS Monterrey version.
        :param browser: Choose which browser use. Available: "chrome" (default), "opera", and "brave".
        :param verbose: print output
        """

        super(Chrome, self).__init__(verbose, blank_passwords)

        if platform.system() != "Darwin":
            raise BadOS("Use your system's OS")

        self.browser = browser()
        if not isinstance(self.browser, BrowserVersion):
            raise BrowserNotImplemented

        self.keys = []
        self._browser_paths = []
        self._database_paths = []

        self.browsers_paths = {
            "chrome": os.path.expanduser("~/Library/Application Support/Google/{ver}/Default"),
            "opera": os.path.expanduser("~/Library/Application Support/{ver}"),
            "brave": os.path.expanduser("~/Library/Application Support/BraveSoftware/{ver}/Default")
        }

        self.browsers_database_paths = {
            "chrome": os.path.expanduser("~/Library/Application Support/Google/{ver}/Default/Login Data"),
            "opera": os.path.expanduser("~/Library/Application Support/{ver}/Login Data"),
            "brave": os.path.expanduser("~/Library/Application Support/BraveSoftware/{ver}/Default/Login Data")
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
        Return database paths and keys for MacOS
        """
        key = self.get_encryption_key()

        if not key:
            raise MacOSKeychainAccessError("Error retrieving the password in the keychain.")

        # Decrypt the keychain key to a hex key
        self.keys.append(PBKDF2(key, b'saltysalt', 16, 1003, hmac_hash_module=SHA1))

        return self.database_paths, self.keys

    def get_encryption_key(self) -> Union[str, None]:
        """
        Return the encryption key for the browser

        Note: The system will notify the user and ask for permission
        even running as a sudo user as it's trying to access the keychain.
        """

        label = "Chrome"  # Default
        # Some browsers have a different safe storage label
        if self.browser == "opera":
            label = "Opera"
        elif self.browser == "brave":
            label = "Brave"

        # Run command
        # Note: this command will prompt a confirmation window
        safe_storage_key = subprocess.check_output(
            f"security 2>&1 > /dev/null find-generic-password -ga '{label}'",
            shell=True)

        # Get key from the output
        return re.findall(r'\"(.*?)\"', safe_storage_key.decode("utf-8"))[0]
