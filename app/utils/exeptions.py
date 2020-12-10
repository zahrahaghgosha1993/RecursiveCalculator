from builtins import Exception


class JsonValidationError(Exception):
    def __init__(self, message, errors):
        self.message = message
        self.errors = errors
