import platform
import sys

from passax.chrome import browsers

if platform.system() == "Windows":
    from passax.chrome import windows as os

elif platform.system() == "Linux":
    from passax.chrome import linux as os

elif platform.system() == "Darwin":
    # Abort because it won't work. The next update will include MacOS browsers.
    sys.exit(-1)
    from passax.chrome import macos as os

else:
    sys.exit(-1)

for browser in browsers.available_browsers:
    passax_ = os.Chrome(browser, blank_passwords=False)  # Class instance
    passax_.fetch()  # Get database paths and keys
    passax_.retrieve_database()  # Get the data from the database
    passax_.save(f"{browser.base_name}_data.txt")
