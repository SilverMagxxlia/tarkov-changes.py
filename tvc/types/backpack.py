from typing import TypedDict

from .cell import Cell
from .item import ItemBase

_Backpack = TypedDict(
    '_Backpack',
    {
        'Blocks Armored Vest': str,
        'Speed Penalty (%)': str,
        'Can be sold on flea market': str,
    },
    total=False,
)


class Backpack(_Backpack, ItemBase, Cell):
    pass
