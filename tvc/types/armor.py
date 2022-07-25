from typing import TypedDict

from .cell import Cell
from .item import ItemBase

_Armor = TypedDict(
    '_Armor',
    {
        'Armor Class': str,
        'Materials': str,
        'Protection Zones': str,
        'Max Durability': str,
        'Effective Durability': float,
        'Movement Speed Penalty': str,
        'Turn Speed Penalty': str,
        'Ergonomics Penalty': str,
        'Blunt Throughput': str,
        'Repair Cost': str,
        'Item Weight': str,
        'Max Stack Size': str,
        'Can be sold on flea market': str,
        'Discard Limit': str,
    },
    total=False,
)


class Armor(_Armor, ItemBase, Cell):
    pass
