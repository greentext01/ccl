class InvalidEventError(RuntimeError):
    def __init__(self, event: str):
        self.event = event

    def __str__(self) -> str:
        return f'Invalid event "{self.event}"\n" \
                "Info: Functions starting with "on_" must be events.'
