from typing import TypedDict

from .cell import Cell
from .item import ItemBase

_BackPack = TypedDict(
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


class BackPack(_BackPack, ItemBase, Cell):
    pass
