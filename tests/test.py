import platform
import unittest
from passaxs import chrome
from passaxs.exceptions import *

sys_ = platform.system()


class TestAll(unittest.TestCase):
    def test_win_browser(self):
        """Not handled win browser"""
        if sys_ == "Windows":
            self.assertRaises(BrowserNotImplemented, lambda: chrome.ChromeWindows(" "))
        else:
            self.assertRaises(BadOS, lambda: chrome.ChromeWindows(" "))

    def test_linux_browser(self):
        """Not handled Linux browser"""
        if sys_ == "Linux":
            self.assertRaises(BrowserNotImplemented, lambda: chrome.ChromeLinux(" "))
        else:
            self.assertRaises(BadOS, lambda: chrome.ChromeLinux(" "))

    def test_get(self):
        """Check if the get_windows / get_linux methods work properly"""
        if sys_ == "Linux":
            r = chrome.ChromeLinux().get_windows()
            self.assertIsInstance(r, tuple)

        elif sys_ == "Windows":
            r = chrome.ChromeWindows().get_windows()
            self.assertIsInstance(r, tuple)

        else:
            self.fail()


if __name__ == '__main__':
    unittest.main()
