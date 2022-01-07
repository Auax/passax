from passax.browser_version import BrowserVersion


class Chrome(BrowserVersion):
    base_name = "chrome"
    versions_win = ['chrome', 'chrome dev', 'chrome beta', 'chrome canary']  # Works
    versions_linux = ['google-chrome', 'google-chrome-unstable', 'google-chrome-beta']  # Works
    versions_mac = ['chrome', 'chrome dev', 'chrome beta', 'chrome canary']  # Testing


class Brave(BrowserVersion):
    base_name = "brave"
    versions_win = ["Brave-Browser", "Brave-Browser-Beta", "Brave-Browser-Nightly"]  # Works
    versions_linux = ["Brave-Browser", "Brave-Browser-Beta", "Brave-Browser-Nightly"]  # Works
    verions_mac = [""]  # Testing


class Opera(BrowserVersion):
    base_name = "opera"
    versions_win = ["Opera Stable", "Opera Next", "Opera Developer"]  # Works
    versions_linux = ["opera", "opera-beta", "opera-developer"]  # Works
    verions_mac = [""]  # Testing


available_browsers = [Chrome, Brave, Opera]
