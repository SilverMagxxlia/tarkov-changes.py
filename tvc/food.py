from __future__ import annotations

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .types.food import Food as FoodPayload

__all__ = ('Food',)


class Food:

    def __init__(self, payload: FoodPayload) -> None:
        self.name: str = payload['Name']
        self.id: str = payload['Item ID']

        self._update(payload)

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other: Food) -> bool:
        return isinstance(other, Food) and self.id == other.id

    def __ne__(self, other: Food) -> bool:
        return not self.__eq__(other)

    def _update(self, data: FoodPayload) -> None:
        self.use_time: int = int(data['Use Time'])
        self.effect_type: str = data['Effect Type']
        self.max_resource: int = int(data['Max Resource'])
        self.stimulator_buffs: str = data['Stimulator Buffs']
        self.health_effects: List[str] = list(data[' Health Effects'])
        self.removes_effects: List[str] = list(data['Removes Effects'])

        self.cell_height: int = int(data['Cell Height'])
        self.width: int = int(data['Cell Width'])
        self.weight: float = float(data['Item Weight'])
        self.max_stack_size: int = int(data['Max Stack Size'])
        self.discard_limit: int = int(data['Discard Limit'])
