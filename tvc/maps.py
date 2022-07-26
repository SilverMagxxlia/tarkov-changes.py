from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .types.maps import Map as MapPayload

__all__ = ('Map',)


class Map:

    def __init__(self, payload: MapPayload) -> None:
        self.name: str = payload['Name']
        self._update(payload)

    def __str__(self) -> str:
        return self.name

    def __int__(self) -> int:
        return self.raid_timer

    def __bool__(self) -> bool:
        return self.enabled

    def __eq__(self, other: Map) -> bool:
        return isinstance(other, Map) and self.internal_name == other.internal_name

    def __ne__(self, other: Map) -> bool:
        return not self.__eq__(other)

    def _update(self, data: MapPayload) -> None:
        self.enabled: bool = data['Map Enabled']
        self.locked: bool = data['Map Locked']
        self.internal_name: str = data['Map Internal Name']
        self.avg_player_level: int = int(data['Avg. Player Level'])
        self.raid_timer: int = data['Raid Timer']
        self.max_players: int = int(data['Max Players'])
        self.min_players: int = int(data['Min Players'])
        self.required_player_level: int = int(data['Required Player Level'])
