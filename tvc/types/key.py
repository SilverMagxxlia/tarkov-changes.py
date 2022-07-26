from typing import Optional, TypedDict

from .cell import Cell
from .item import ItemBase

_Key = TypedDict(
    '_Key',
    {
        'Fixed Price': Optional[int],
        'Unlootable': str,
        'Discarding Block': str,
        'MaximumNumber Of Usage': str,
    },
    total=False,
)


class Key(_Key, ItemBase, Cell):
    pass
