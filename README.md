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
Passax **v-1.10** now includes:
- MacOS (Only tried in Monterrey)
- Windows (Only tried in Win-10)
- Linux (Tried on Ubuntu / Kali Linux)

---
## Usage

_Notice that sometimes you might get a blank output, this can be because you had installed the browser you're trying to
get data from, but the login data was erased._

**Print to screen the login info from Chrome.**

```python
from passax import chrome

# Change to chrome.ChromeLinux for Linux users.
# Chrome is a handled browser
windows = chrome.ChromeWindows("chrome")  # Class instance
windows.get_windows()  # Get database paths and keys
windows.retrieve_database()  # Get the data from the database
print(windows.pretty_print())
```

**Save data to a file.**

```python
from passax import chrome

windows = chrome.ChromeWindows("chrome")
windows.get_windows()
windows.retrieve_database()
windows.save("login_data.txt")
```

**Save login data from all suported browsers**

```python
from passax import chrome

for browser in chrome.available_browsers:
    windows = chrome.ChromeWindows(browser)
    windows.get_windows()
    windows.retrieve_database()
    windows.save(f"{browser}.txt")
```
---

## Contact

Any suggestions/problems contact me at **auax.dev@gmail.com**