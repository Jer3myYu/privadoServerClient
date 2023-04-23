class PSException(Exception):
    """Base clase for privado server exception."""
    def __init__(self, error, detail):
        self.err = err
        self.detail = detail

class SubprocessError(PSException):
    def __init__(self, e):
        super().__init__("Subprocess Uncaught Error", e)

class SubprocessUnzipError(PSException):
    def __init__(self, e):
        super().__init__("Subprocess Unzip Error", e)