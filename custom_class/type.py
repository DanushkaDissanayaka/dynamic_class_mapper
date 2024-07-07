class Type:

    alias:str
    default_factory:callable

    def __init__(self, alias:str = None, default_factory:callable = None) -> None:
        self.alias = alias
        self.default_factory = default_factory