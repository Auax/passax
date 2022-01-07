import platform

import passax.exceptions
from passax.chrome.base import ChromeBase

sys_ = platform.system()
if sys_ == "Linux":
    from passax.chrome.linux import Chrome
elif sys_ == "Windows":
    from passax.chrome.windows import Chrome
elif sys_ == "Darwin":
    from passax.chrome.macos import Chrome

else:
    raise passax.exceptions.BadOS("No compatible OS detected!")
