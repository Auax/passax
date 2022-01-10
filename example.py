import platform
import sys

from passax.chrome import browsers

if platform.system() == "Windows":
    from passax.chrome import windows as os

elif platform.system() == "Linux":
    from passax.chrome import linux as os

elif platform.system() == "Darwin":
    from passax.chrome import macos as os

else:
    print("No compatible system!")
    sys.exit(-1)  # Clean exit

for browser in browsers.available_browsers:
    passax_ = os.Chrome(browser, blank_passwords=False)  # Class instance
    passax_.fetch()  # Get database paths and keys
    passax_.retrieve_database()  # Get the data from the database
    passax_.save(f"{browser.base_name}_data.txt", blank_file=False, verbose=True)
