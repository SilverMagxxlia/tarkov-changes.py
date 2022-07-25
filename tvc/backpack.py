from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .types.backpack import Backpack as BackPackPayload

__all__ = ('BackPack',)


class Backpack:

    def __init__(self, payload: BackPackPayload) -> None:
        self.name: str = payload['Name']
        self.id: str = payload['Item ID']
        self.blocks_armor_vest: bool = 'true' == payload['Blocks Armored Vest']

        self._update(payload)

    def _update(self, data: BackPackPayload) -> None:
        self.speed_penalty_percent: int = int(data['Speed Penalty (%)'])
        self.cell_height: int = int(data['Cell Height'])
        self.cell_width: int = int(data['Cell Width'])

        self.weight: float = float(data['Item Weight'])
        self.banned_on_flea: bool = data['Can be sold on flea market'] == 'false'
        self.discard_limit: int = int(data['Discard Limit'])
        self.max_stack_size: int = int(data['Max Stack Size'])
