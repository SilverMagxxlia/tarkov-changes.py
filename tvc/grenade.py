from __future__ import annotations

from typing import TYPE_CHECKING

from .mixins import Hashable

if TYPE_CHECKING:
    from .types.grenade import Grenade as GrenadePayload

__all__ = ('Grenade',)


class Grenade(Hashable):

    def __init__(self, payload: GrenadePayload) -> None:
        self.name: str = payload['Name']
        self.id: str = payload['Item ID']

        self._update(payload)

    def __str__(self) -> str:
        return self.name

    @property
    def image_url(self):
        return f'https://tarkov-changes.com/img/items/128/{self.id}.png'

    def _update(self, data: GrenadePayload) -> None:
        self.can_hide_during_throw: bool = 'true' == data['Can Be Hidden During Throw']
        self.contusion_distance: int = int(data['Contusion Distance'])
        self.explosion_delay: float = float(data['Explosion Delay'])
        self.fragments_count: int = int(data['Fragments Count'])
        self.max_explosion_distance: int = int(data['Max Explosion Distance'])
        self.min_explosion_distance: int = int(data['Min Explosion Distance'])
        self.strength: int = int(data['Strength'])
        self.cell_height: int = int(data['Cell Height'])
        self.cell_width: int = int(data['Cell Width'])
        self.weight: float = float(data['Item Weight'])
        self.banned_on_flea: bool = data['Can be sold on flea market'] == 'false'
        self.max_stack_size: int = int(data['Max Stack Size'])
        self.discard_limit: int = int(data['Discard Limit'])
