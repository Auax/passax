import platform
import sys

from passax.chrome.browsers import Brave, Opera

if platform.system() == "Windows":
    from passax.chrome import windows as os

elif platform.system() == "Linux":
    from passax.chrome import linux as os

elif platform.system() == "Darwin":
    # Abort because it won't work. The next update will include macOS browsers.
    from passax.chrome import macos as os

else:
    sys.exit(-1)

passax_ = os.Chrome(Opera, blank_passwords=False)  # Class instance
passax_.fetch()  # Get database paths and keys
passax_.retrieve_database()  # Get the data from the database
print(passax_.pretty_print())
