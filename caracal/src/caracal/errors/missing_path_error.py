class MissingPathError(RuntimeError):
    def __init__(self, path: str):
        self.path = path

    def __str__(self) -> str:
        return f'Path "{self.path}" does not exist'
