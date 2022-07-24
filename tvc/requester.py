
from __future__ import annotations

import json
import aiohttp
import asyncio

from typing import (
    Any,
    ClassVar,
    Coroutine,
    Optional,
    Union,
    Dict,
    List,
    TypeVar,
    TYPE_CHECKING,
)

from urllib.parse import quote as _uriquote

from . import utils
from .exceptions import InvalidRequest

if TYPE_CHECKING:
    from .types.armor import Armor as ArmorPayload
    from .types.ammunition import Ammunition as AmmunitionPayload

    T = TypeVar('T')
    BE = TypeVar('BE', bound=BaseException)
    MU = TypeVar('MU', bound='MaybeUnlock')
    Response = Coroutine[Any, Any, T]


async def json_or_text(response: aiohttp.ClientResponse) -> Union[Dict[str, Any], str]:
    text = await response.text(encoding='utf-8')

    try:

        if response.headers['content-type'] == 'application/json':
            return json.loads(text)

    except KeyError:
        pass

    return text


class Route:
    BASE: ClassVar[str] = 'https://api.tarkov-changes.com/v1'

    def __init__(self, method: str, path: str, **parameters: Any):
        self.path: str = path
        self.method: str = method

        url = "{}{}".format(self.BASE, path)

        if parameters:
            url = url.format_map({k: _uriquote(v) if isinstance(v, str) else v for k, v in parameters.items()})

        self.url = url


class HTTPRequester:

    def __init__(
        self,
        *,
        token: str,
        session: aiohttp.ClientSession = aiohttp.ClientSession(),
        loop: Optional[asyncio.AbstractEventLoop] = None,
    ) -> None:
        self._loop: asyncio.AbstractEventLoop = asyncio.get_event_loop() if loop is None else loop
        self._session = session
        self.token: str = token

    async def request(self, route: Route, **kwargs: Any) -> Any:
        method = route.method
        url = route.url

        headers: Dict[str, str] = {
            "AUTH-TOKEN": self.token,
        }

        if 'json' in kwargs:
            headers['Content-Type'] = 'application/json'
            kwargs['data'] = utils._to_json(kwargs.pop('json'))

        kwargs['headers'] = headers

        async with self._session.request(method, url, **kwargs) as response:
            data = await json_or_text(response)

            if response.status == 401:
                raise InvalidRequest(
                    response.status,
                    status=data['status'],
                    msg=data['msg'],
                    result=data['result']
                )

            if 300 > response.status >= 200:
                return data['results']

    def get_ammunition(self, query: str = None) -> Response[List[AmmunitionPayload]]:
        url = 'ammo'

        if query:
            url += f'?query={query}'

        r = Route('GET', url)
        return self.request(r)

    def get_armor(self, query: str = None) -> Response[List[ArmorPayload]]:
        url = 'armor'

        if query:
            url += f'?query={query}'

        r = Route('GET', url)
        return self.request(r)