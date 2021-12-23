import platform

import passax.exceptions
from passax.chrome.base import ChromeBase

sys_ = platform.system()
if sys_ == "Linux":
    from passax.chrome.linux import ChromeLinux
elif sys_ == "Windows":
    from passax.chrome.windows import ChromeWindows
elif sys_ == "Darwin":
    from passax.chrome.macos import ChromeMacOS

else:
    raise passax.exceptions.BadOS("No compatible OS detected!")

available_browsers = ChromeBase.available_browsers
