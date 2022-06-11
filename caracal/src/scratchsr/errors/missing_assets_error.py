class MissingAssetsError(RuntimeError):
    def __init__(self, dir: str):
        self.dir = dir

    def __str__(self) -> str:
        return f'Missing "assets" directory in "{self.dir}"'
