from passax.browser_version import BrowserVersion


class Chrome(BrowserVersion):
    base_name = "chrome"
    versions_win = ["chrome", "chrome dev", "chrome beta", "chrome canary"]
    versions_linux = ["google-chrome", "google-chrome-unstable", "google-chrome-beta"]
    versions_mac = ["chrome", "chrome dev", "chrome beta", "chrome canary"]


class Brave(BrowserVersion):
    base_name = "brave"
    versions_win = ["Brave-Browser", "Brave-Browser-Beta", "Brave-Browser-Nightly"]
    versions_linux = ["Brave-Browser", "Brave-Browser-Beta", "Brave-Browser-Nightly"]
    versions_mac = ["Brave-Browser", "Brave-Browser-Beta", "Brave-Browser-Nightly"]


class Opera(BrowserVersion):
    base_name = "opera"
    versions_win = ["Opera Stable", "Opera Next", "Opera Developer"]
    versions_linux = ["opera", "opera-beta", "opera-developer"]
    versions_mac = ["com.operasoftware.Opera", "com.operasoftware.OperaNext", "com.operasoftware.OperaDeveloper"]


available_browsers = [Chrome, Brave, Opera]
