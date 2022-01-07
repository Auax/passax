# Passax

**EDUCATIONAL PURPOSES ONLY**

**Python3** library that can retrieve Chrome-based browser's saved login info.

---

## Requirements

- `secretstorage~=3.3.1`
- `pywin32==302` _(Only Windows)_
- `pycryptodome==3.12.0`

Notice that these libraries will be automatically installed through the `setup.py`
file when using `pip install passax`.

---

## Suported Systems

Passax **v-1.20** now includes:

- MacOS (Only tried in Monterrey) `[Prepared, but I need to include the browser names in browsers.py]`
- Windows (Only tried in Win-10)
- Linux (Tried on Ubuntu / Kali Linux)

---

## Usage

_Notice that sometimes you might get a blank output, this can be because you had installed the browser you're trying to
get data from, but the login data was erased._

**Print to screen the login info from Chrome.**

```python
from passax.chrome import windows, browsers

# Change to chrome.ChromeLinux for Linux users.
# Change to chrome.ChromeMacOS for MacOS users.
# Chrome is a supported browser
win = windows.Chrome(browsers.Chrome, blank_passwords=False)  # Class instance
win.fetch()  # Get database paths and keys
win.retrieve_database()  # Get the data from the database
print(win.pretty_print())
```

**Save data to a file.**

```python
from passax.chrome import windows, browsers

win = windows.Chrome(browsers.Chrome, blank_passwords=False)
win.fetch()
win.retrieve_database()
win.save("login_data.txt")
```

**Save login data from all suported browsers**

```python
from passax.chrome import windows, browsers

for browser in browsers.available_browsers:
    win = windows.Chrome(browser, blank_passwords=False)  # Class instance
    win.fetch()  # Get database paths and keys
    win.retrieve_database()  # Get the data from the database
    win.save(f"{browser.base_name}_data.txt")  # Save the file
```

**Run in any supported OS** (Note that macOS will not work because I need to include the browsers. This will come with
the next update)

```python
import platform
import sys

from passax.chrome import browsers

if platform.system() == "Windows":
    from passax.chrome import windows as os

elif platform.system() == "Linux":
    from passax.chrome import linux as os

elif platform.system() == "Darwin":
    # Abort because it won't work. The next update will include macOS browsers.
    sys.exit(-1)
    from passax.chrome import macos as os

else:
    sys.exit(-1)

for browser in browsers.available_browsers:
    passax_ = os.Chrome(browser, blank_passwords=False)  # Class instance
    passax_.fetch()  # Get database paths and keys
    passax_.retrieve_database()  # Get the data from the database
    passax_.save(f"{browser.base_name}_data.txt")
```

---

## Contact

Any suggestions/problems contact me at **auax.dev@gmail.com**