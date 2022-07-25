from typing import TypedDict

from .cell import Cell
from .item import ItemBase

_Backpack = TypedDict(
    '_BackPack',
    {
        'Blocks Armored Vest': str,
        'Speed Penalty (%)': str,
        'Item Weight': str,
        'Can be sold on flea market': str,
        'Discard Limit': str,
        'Max Stack Size': str,
    },
    total=False,
)


class Backpack(_Backpack, ItemBase, Cell):
    pass
