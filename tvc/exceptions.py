from __future__ import annotations

from typing import Any, Dict, Union, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from aiohttp import ClientResponse

    try:
        from requester import Response

        _ResponseType = Union[ClientResponse, Response]

    except ModuleNotFoundError:
        _ResponseType = ClientResponse

__all__ = (
    'TVCException',
    'RequesterException',
    'InvalidRequest',
    'NotFound',
)


class TVCException(Exception):
    pass


class RequesterException(TVCException):

    def __init__(
        self,
        response: _ResponseType,
        message: Optional[Union[str, Dict[str, Any]]]
    ) -> None:
        self.response: _ResponseType = response
        self.status: int = response.status

        self.text: str

        if isinstance(message, dict):
            self.text = message.get('msg')

        else:
            self.text = message or ""

        fmt = "{0.status} {0.reason} (error code: {1})"

        if len(self.text):
            fmt += ": {2}"

        super().__init__(fmt.format(self.response, self.status, self.text))


class InvalidRequest(RequesterException):
    pass


class NotFound(RequesterException):
    pass
