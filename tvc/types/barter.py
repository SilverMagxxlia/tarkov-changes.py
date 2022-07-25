from typing import TypedDict

from .cell import Cell
from .item import ItemBase

_Barter = TypedDict(
    '_Barter',
    {
        'Examine EXP': str,
        'Quest Only Item': str,
        'Item Weight': str,
        'Max Stack Size': str,
        'Discard Limit': str,
    },
    total=False,
)


class Barter(_Barter, ItemBase, Cell):
    pass
