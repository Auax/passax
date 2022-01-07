import platform
import unittest
from passax import chrome
from passax.exceptions import *

sys_ = platform.system()


class TestAll(unittest.TestCase):
    def test_win_browser(self):
        """Not handled win browser"""
        if sys_ == "Windows":
            self.assertRaises(BrowserNotImplemented, lambda: chrome.Chrome(" "))
        else:
            self.assertRaises(BadOS, lambda: chrome.Chrome(" "))

    def test_linux_browser(self):
        """Not handled Linux browser"""
        if sys_ == "Linux":
            self.assertRaises(BrowserNotImplemented, lambda: chrome.Chrome(" "))
        else:
            self.assertRaises(BadOS, lambda: chrome.Chrome(" "))


if __name__ == '__main__':
    unittest.main()
