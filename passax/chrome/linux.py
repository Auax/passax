import os
import platform
from typing import Type, Union

import secretstorage
from Crypto.Protocol.KDF import PBKDF2

from passax.browser_version import BrowserVersion
from passax.chrome import browsers
from passax.chrome.base import ChromeBase
from passax.exceptions import *


class Chrome(ChromeBase):
    """ Decryption class for Chrome in Linux OS """

    def __init__(self,
                 browser: Type[BrowserVersion] = browsers.Chrome,
                 verbose: bool = False,
                 blank_passwords: bool = False):
        """
        Decryption class for Linux.
        :param browser: Choose which browser use.
        :param verbose: print output
        :param blank_passwords: save or not blank passwords
        """

        super(Chrome, self).__init__(verbose, blank_passwords)

        if platform.system() != "Linux":
            raise BadOS("Use a Linux system for this class.")

        self.browser = browser()
        if not isinstance(self.browser, BrowserVersion):
            raise BrowserNotImplemented

        # This is where all the paths for the installed browsers will be saved
        self._browser_paths = []
        self._database_paths = []

        self.keys = []
        base_path = os.getenv('HOME')

        self.browsers_paths = {
            "chrome": base_path + "/.config/{ver}/Default",
            "opera": base_path + "/.config/{ver}",
            "brave": base_path + "/.config/BraveSoftware/{ver}/Default"
        }
        self.browsers_database_paths = {
            "chrome": base_path + "/.config/{ver}/Default/Login Data",
            "opera": base_path + "/.config/{ver}/Login Data",
            "brave": base_path + "/.config/BraveSoftware/{ver}/Default/Login Data"
        }

    @property
    def browser_paths(self):
        return self._browser_paths

    @property
    def database_paths(self):
        # Return all database paths
        return self._database_paths

    @ChromeBase.get
    def fetch(self):
        """
        Return database paths and keys for Linux
        """

        key = self.get_encryption_key()

        if not key:
            raise LinuxSafeStorageError("Error retrieving the password in Safe Storage.")

        self.keys.append(key)
        return self.database_paths, self.keys

    def get_encryption_key(self) -> bytes:
        """
        Return the encryption key for the browser
        """
        label = "Chrome Safe Storage"  # Default
        # Some browsers have a different safe storage label
        if self.browser == "opera":
            label = "Chromium Safe Storage"
        elif self.browser == "brave":
            label = "Brave Safe Storage"

        # Default password is peanuts
        passw = 'peanuts'.encode('utf8')
        # New connection to session bus
        bus = secretstorage.dbus_init()
        collection = secretstorage.get_default_collection(bus)
        for item in collection.get_all_items():  # Iterate
            if item.get_label() == label:
                passw = item.get_secret().decode("utf-8")  # Retrieve item
                break

        return PBKDF2(passw, b'saltysalt', 16, 1)
