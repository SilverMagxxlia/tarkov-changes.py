from __future__ import annotations

from typing import List, TYPE_CHECKING

from .mixins import Hashable

if TYPE_CHECKING:
    from .types.armor import Armor as ArmorPayload

__all__ = ('Armor',)


class Armor(Hashable):

    __slots__ = (
        'id',
        'name',
        'armor_class',
        'materials',
        'protection_zones',
        'max_durability',
        'effective_durability',
        'movement_speed_penalty',
        'turn_speed_penalty',
        'blunt_throughput',
        'repair_cost',
        'cell_height',
        'cell_width',
        'weight',
        'banned_on_flea',
        'discard_limit',
    )

    def __init__(self, payload: ArmorPayload) -> None:
        self.name: str = payload['Name']
        self.id: str = payload['Item ID']
        self.armor_class: int = int(payload['Armor Class'])
        self.materials: str = payload['Materials']
        self.protection_zones: List[str] = list(payload['Protection Zones'])

        self._update(payload)

    def __str__(self) -> str:
        return self.name

    def _update(self, data: ArmorPayload) -> None:
        self.max_durability: int(data['Max Durability'])
        self.effective_durability: float = data['Effective Durability']
        self.movement_speed_penalty: int = int(data['Movement Speed Penalty'])
        self.turn_speed_penalty: int = int(data['Turn Speed Penalty'])
        self.blunt_throughput: float = float(data['Blunt Throughput'])
        self.repair_cost: int = int(data['Repair Cost'])
        self.cell_height: int = int(data['Cell Height'])
        self.cell_width: int = int(data['Cell Width'])
        self.weight: float = float(data['Item Weight'])
        self.banned_on_flea: bool = data['Can be sold on flea market'] == 'false'
        self.discard_limit: int = int(data['Discard Limit'])
