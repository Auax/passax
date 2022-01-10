class Error(Exception):
    """
    Base class for other exceptions
    """

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return self.message if self.message else "  "


class DatabaseError(Error):
    def __init__(self, *args):
        Error.__init__(self, *args)


class DatabaseIsLocked(Error):
    def __init__(self, *args):
        Error.__init__(self, *args)


class DatabaseUndefinedTable(Error):
    def __init__(self, *args):
        Error.__init__(self, *args)


class DatabaseNotFound(Error):
    def __init__(self, *args):
        Error.__init__(self, *args)


class OSNotSupported(Error):
    def __init__(self, *args):
        Error.__init__(self, *args)


class BadOS(Error):
    def __init__(self, *args):
        Error.__init__(self, *args)


class BrowserNotImplemented(Error):
    def __init__(self, *args):
        Error.__init__(self, *args)


class MacOSKeychainAccessError(Error):
    def __init__(self, *args):
        Error.__init__(self, *args)


class LinuxSafeStorageError(Error):
    def __init__(self, *args):
        Error.__init__(self, *args)
