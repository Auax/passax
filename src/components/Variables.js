// All example codes and xml icons will be here

export const exampleCode1 = `from passax.chrome import windows, browsers

win = windows.Chrome(browsers.Chrome, blank_passwords=False)
win.fetch()  # Get database paths and keys
win.retrieve_database()  # Get the data from the database
print(win.pretty_print())`;

export const exampleCode2 = `from passax.chrome import windows, browsers

for browser in browsers.available_browsers:
    win = windows.Chrome(browser, blank_passwords=False)
    # Get database paths and keys
    win.fetch()
    # Get the data from the database
    win.retrieve_database()
    # Save the file
    win.save(f"{browser.base_name}_data.txt", blank_file=False, verbose=True)`

export const exampleCode3 = `import platform
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
    passax_.save(f"{browser.base_name}_data.txt", blank_file=False, verbose=True)`


export let light_icon = (
    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 stroke-stone-800" fill="none" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
    </svg>
)

export let dark_icon = (
    <svg viewBox="0 0 24 24" fill="none" className="w-6 h-6">
        <path fillRule="evenodd" clipRule="evenodd"
              d="M17.715 15.15A6.5 6.5 0 0 1 9 6.035C6.106 6.922 4 9.645 4 12.867c0 3.94 3.153 7.136 7.042 7.136 3.101 0 5.734-2.032 6.673-4.853Z"
              className="fill-sky-400/20"/>
        <path
            d="m17.715 15.15.95.316a1 1 0 0 0-1.445-1.185l.495.869ZM9 6.035l.846.534a1 1 0 0 0-1.14-1.49L9 6.035Zm8.221 8.246a5.47 5.47 0 0 1-2.72.718v2a7.47 7.47 0 0 0 3.71-.98l-.99-1.738Zm-2.72.718A5.5 5.5 0 0 1 9 9.5H7a7.5 7.5 0 0 0 7.5 7.5v-2ZM9 9.5c0-1.079.31-2.082.845-2.93L8.153 5.5A7.47 7.47 0 0 0 7 9.5h2Zm-4 3.368C5 10.089 6.815 7.75 9.292 6.99L8.706 5.08C5.397 6.094 3 9.201 3 12.867h2Zm6.042 6.136C7.718 19.003 5 16.268 5 12.867H3c0 4.48 3.588 8.136 8.042 8.136v-2Zm5.725-4.17c-.81 2.433-3.074 4.17-5.725 4.17v2c3.552 0 6.553-2.327 7.622-5.537l-1.897-.632Z"
            className="fill-sky-500"/>
        <path fillRule="evenodd" clipRule="evenodd"
              d="M17 3a1 1 0 0 1 1 1 2 2 0 0 0 2 2 1 1 0 1 1 0 2 2 2 0 0 0-2 2 1 1 0 1 1-2 0 2 2 0 0 0-2-2 1 1 0 1 1 0-2 2 2 0 0 0 2-2 1 1 0 0 1 1-1Z"
              className="fill-sky-500"/>
    </svg>
)