from typing import TypedDict

from .cell import Cell
from .item import ItemBase

_Key = TypedDict(
    '_Key',
    {
        'Fixed Price': int | None,
        'Unlootable': str,
        'Discarding Block': str,
        'MaximumNumber Of Usage': str,
        'Item Weight': str,
        'Max Stack Size': str,
        'Discard Limit': str,
    },
    total=False,
)


class Key(_Key, ItemBase, Cell):
    pass
