class MissingFieldError(RuntimeError):
    def __init__(self, field: str):
        self.field = field

    def __str__(self) -> str:
        return f'Missing field "{self.field}"'
