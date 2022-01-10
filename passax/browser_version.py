class BrowserVersion:
    """
    Simple global class
    Note: self.base_name is defined in the child classes
    """

    def __str__(self) -> str:
        return self.base_name

    def __eq__(self, __o: object) -> bool:
        return self.base_name == __o
