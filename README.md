# Passax

**EDUCATIONAL PURPOSES ONLY**

**Python3** library that can retrieve Chrome-based browser's saved login info.

---

## Websites

<h2><img src="https://user-images.githubusercontent.com/16353807/151009140-8fc0548e-4c9b-4a93-8bc4-e8ea5c36de36.png" width="20" height="20" style="display:none;"/>   <a href="https://pypi.org/project/passax/">Passax in PYPI</a></h2>

<h2><img src="https://user-images.githubusercontent.com/16353807/151010585-465c85fb-9aca-4556-9f97-a866bf8242ed.png" width="20" height="20" style="display:none;"/>   <a href="https://auax.github.io/passax/">Passax official website</a></h2>


## Requirements

- `secretstorage~=3.3.1`
- `pywin32==302` _(Only Windows)_
- `pycryptodome==3.12.0`

Notice that these libraries will be automatically installed through the `setup.py`
file when using `pip install passax`.

---

## Supported Systems

Passax **v-1.10** now includes:

- macOS (Only tried in Monterrey)
- Windows (Only tried in Win-10)
- Linux (Tried on Ubuntu / Kali Linux)

---

## Usage

_Notice that sometimes you might get a blank output, this can be because you had installed the browser you're trying to
get data from, but the login data was erased.
You can use the `blank_file = False` parameter not to save the file if it's blank._

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
win.save("login_data.txt", blank_file=False, verbose=True)
```

**Save login data from all supported browsers.**

```python
from passax.chrome import windows, browsers

for browser in browsers.available_browsers:
    win = windows.Chrome(browser, blank_passwords=False)  # Class instance
    win.fetch()  # Get database paths and keys
    win.retrieve_database()  # Get the data from the database
    win.save(f"{browser.base_name}_data.txt", blank_file=False, verbose=True)  # Save the file
```

**Run in any supported OS.**

```python
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

```

---

## To do

* Add the test file back (removed because it needed a fix)
* Maybe add other browsers not based on Chromium (Firefox, for example).

---

## Contact

Any suggestions/problems contact me at **auax.dev@gmail.com**
