from __future__ import annotations

import aiohttp

from typing import Dict, Optional, List
from asyncio import get_event_loop, AbstractEventLoop

from .ammunition import Ammunition
from .armor import Armor
from .backpack import Backpack
from .barter import Barter
from .food import Food
from .grenade import Grenade
from .headphone import Headphone
from .item import Item
from .key import Key
from .maps import Map
from .requester import HTTPRequester

__all__ = ('TVCClient',)


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
        self._backpacks: Dict[str, Backpack] = {}
        self._barters: Dict[str, Barter] = {}
        self._foods: Dict[str, Food] = {}
        self._grenades: Dict[str, Grenade] = {}
        self._items: Dict[str, Item] = {}
        self._keys: Dict[str, Key] = {}
        self._maps: Dict[str, Map] = {}

    def start(self) -> None:
        self.loop.run_until_complete(self.load_endpoints())

    def get_ammunition(self, name: str) -> Optional[Ammunition]:
        return self._ammunition.get(name)

    def get_armor(self, name: str) -> Optional[Armor]:
        return self._armors.get(name)

    def get_backpack(self, name: str) -> Optional[Backpack]:
        return self._backpacks.get(name)

    def get_barter(self, name: str) -> Optional[Barter]:
        return self._barters.get(name)

    def get_food(self, name: str) -> Optional[Food]:
        return self._foods.get(name)

    def get_grenade(self, name: str) -> Optional[Grenade]:
        return self._grenades.get(name)

    def get_item(self, name: str) -> Optional[Item]:
        return self._items.get(name)

    def get_key(self, name: str) -> Optional[Key]:
        return self._keys.get(name)

    async def load_endpoints(self) -> None:
        self._clear()

        armors = await self.fetch_armor()
        ammunition = await self.fetch_ammunition()
        backpacks = await self.fetch_backpack()
        barters = await self.fetch_barter()
        foods = await self.fetch_food()
        grenades = await self.fetch_grenade()
        items = await self.fetch_item()
        keys = await self.fetch_key()
        maps = await self.fetch_map()

        for armor in armors:
            self._armors[armor.name] = armor

        for ammo in ammunition:
            self._ammunition[ammo.name] = ammo

        for backpack in backpacks:
            self._backpacks[backpack.name] = backpack

        for barter in barters:
            self._barters[barter.name] = barter

        for food in foods:
            self._foods[food.name] = food

        for grenade in grenades:
            self._grenades[grenade.name] = grenade

        for item in items:
            self._items[item.name] = item

        for key in keys:
            self._keys[key.name] = key

        for _map in maps:
            self._maps[_map] = _map

    async def fetch_ammunition(self, query: str = None) -> List[Ammunition]:
        data = await self.__requester.get_ammunition(query)
        return [Ammunition(d) for d in data]

    async def fetch_armor(self, query: str = None) -> List[Armor]:
        data = await self.__requester.get_armor(query)
        return [Armor(d) for d in data]

    async def fetch_backpack(self, query: str = None) -> List[Backpack]:
        data = await self.__requester.get_backpack(query)
        return [Backpack(d) for d in data]

    async def fetch_barter(self, query: str = None) -> List[Barter]:
        data = await self.__requester.get_barter(query)
        return [Barter(d) for d in data]

    async def fetch_food(self, query: str = None) -> List[Food]:
        data = await self.__requester.get_food(query)
        return [Food(d) for d in data]

    async def fetch_grenade(self, query: str = None) -> List[Grenade]:
        data = await self.__requester.get_grenade(query)
        return [Grenade(d) for d in data]

    async def fetch_headphone(self, query: str = None) -> List[Headphone]:
        data = await self.__requester.get_headphone(query)
        return [Headphone(d) for d in data]

    async def fetch_item(self, query: str = None) -> List[Item]:
        data = await self.__requester.get_item(query)
        return [Item(d) for d in data]

    async def fetch_key(self, query: str = None) -> List[Key]:
        data = await self.__requester.get_key(query)
        return [Key(d) for d in data]

    async def fetch_map(self, query: str = None) -> List[Map]:
        data = await self.__requester.get_map(query)
        return [Map(d) for d in data]

    async def fetch_banned_item_names(self) -> List[str]:
        data = await self.__requester.get_banned()
        return [d['Name'] for d in data]

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

    @property
    def backpacks(self) -> List[Backpack]:
        return list(self._backpacks.values())

    @property
    def barters(self) -> List[Barter]:
        return list(self._barters.values())

    @property
    def foods(self) -> List[Food]:
        return list(self._foods.values())

    @property
    def grenades(self) -> List[Grenade]:
        return list(self._grenades.values())

    @property
    def items(self) -> List[Item]:
        return list(self._items.values())

    @property
    def keys(self) -> List[Key]:
        return list(self._keys.values())

    @property
    def maps(self) -> List[Map]:
        return list(self._maps.values())
