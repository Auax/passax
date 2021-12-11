import platform
from passax.chrome.base import ChromeBase

sys_ = platform.system()
if sys_ == "Linux":
    from passax.chrome.linux import ChromeLinux
elif sys_ == "Windows":
    from passax.chrome.windows import ChromeWindows

available_browsers = ChromeBase.available_browsers
