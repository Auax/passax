import os
import platform

import secretstorage
from Crypto.Protocol.KDF import PBKDF2

from passax.chrome.base import ChromeBase
from passax.exceptions import *


class ChromeLinux(ChromeBase):
    """ Decryption class for Chrome in Linux OS """

    def __init__(self, browser: str = "chrome", verbose: bool = False, blank_passwords: bool = False):
        """
        Decryption class for Linux.
        :param browser: Choose which browser use. Available: "chrome" (default), "opera", and "brave".
        :param verbose: print output
        """

        super(ChromeLinux, self).__init__(verbose, blank_passwords)

        if platform.system() != "Linux":
            raise BadOS("Use your system's OS")

        if not browser.lower() in self.available_browsers:
            raise BrowserNotImplemented

        self.key = []
        self.browser = browser.lower()
        base_path = os.getenv('HOME')

        self.browsers_paths = {
            "chrome": base_path + "/.config/google-chrome/Default/",
            "opera": base_path + "/.config/opera/",
            "brave": base_path + "/.config/BraveSoftware/Brave-Browser/Default"
        }

        self.browsers_database_paths = {
            "chrome": base_path + "/.config/google-chrome/Default/Login Data",
            "opera": base_path + "/.config/opera/Login Data",
            "brave": base_path + "/.config/BraveSoftware/Brave-Browser/Default/Login Data"
        }

    def get_linux(self):
        """
        Return database paths and keys for Linux
        """

        passw = 'peanuts'.encode('utf8')  # Set default
        bus = secretstorage.dbus_init()  # New connection to session bus
        collection = secretstorage.get_default_collection(bus)
        for item in collection.get_all_items():  # Iterate
            if item.get_label() == 'Chrome Safe Storage':
                passw = item.get_secret().decode("utf-8")  # Retrieve item
                break

        self.key = PBKDF2(passw, b'saltysalt', 16, 1)
        return [self.browsers_database_paths[self.browser]], [self.key]

    @property
    def database_paths(self):
        # Return all database paths
        return [self._database_paths]
