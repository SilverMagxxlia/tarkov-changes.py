from __future__ import annotations

import aiohttp

from typing import Dict, Optional, List
from asyncio import get_event_loop, AbstractEventLoop

from .ammunition import Ammunition
from .armor import Armor
from .requester import HTTPRequester


class TVCClient:

    def __init__(
        self,
        token: str,
        loop: Optional[AbstractEventLoop] = None,
        session: aiohttp.ClientSession = aiohttp.ClientSession(),
    ) -> None:
        self.loop: AbstractEventLoop = get_event_loop() if loop is None else loop
        self.__requester: HTTPRequester = HTTPRequester(token=token, session=session, loop=loop)
        self.token: str = token

        self._clear()

    def _clear(self) -> None:
        self._ammunition: Dict[str, Ammunition] = {}
        self._armors: Dict[str, Armor] = {}

    def start(self) -> None:
        self.loop.run_until_complete(self.load_endpoints())

    async def load_endpoints(self) -> None:
        self._clear()

        armors = await self.fetch_armor()
        ammunition = await self.fetch_ammunition()

        for armor in armors:
            self._armors[armor.name] = armor

        for ammo in ammunition:
            self._ammunition[ammo.name] = ammo

    async def fetch_ammunition(self, query: str = None) -> List[Ammunition]:
        data = await self.__requester.get_ammunition(query)
        return [Ammunition(d) for d in data]

    async def fetch_armor(self, query: str = None) -> List[Armor]:
        data = await self.__requester.get_armor(query)
        return [Armor(d) for d in data]

    async def __aenter__(self) -> TVCClient:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.__requester._session.close()

    @property
    def ammunition(self) -> List[Ammunition]:
        return list(self._ammunition.values())

    @property
    def armors(self) -> List[Armor]:
        return list(self._armors.values())
