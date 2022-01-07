class BrowserVersion:
    """Simple global class"""
    def __str__(self) -> str:
        return self.base_name

    def __eq__(self, __o: object) -> bool:
        return self.base_name == __o
