from __future__ import annotations

from typing import TYPE_CHECKING

from .mixins import Hashable

if TYPE_CHECKING:
    from .types.barter import Barter as BarterPayload

__all__ = ('Barter',)


class Barter(Hashable):

    def __init__(self, payload: BarterPayload) -> None:
        self.name: str = payload['Name']
        self.id: str = payload['Item ID']

        self._update(payload)

    def _update(self, data: BarterPayload) -> None:
        self.examine_exp: int = int(data['Examine EXP'])
        self.quest_only_item: bool = 'true' == data['Quest Only Item']

        self.cell_height: int = int(data['Cell Height'])
        self.cell_width: int = int(data['Cell Width'])
        self.weight: float = float(data['Item Weight'])
        self.max_stack_size: int = int(data['Max Stack Size'])
        self.discard_limit: int = int(data['Discard Limit'])
