class TVCException(Exception):

    def __init__(self, code: int, status: str, msg: str, result: str) -> None:
        self.status: str = status
        self.msg: str = msg
        self.result: str = result
        self.code: int = code


class InvalidRequest(TVCException):
    pass
