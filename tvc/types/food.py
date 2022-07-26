from typing import TypedDict

from .cell import Cell
from .item import ItemBase

_Food = TypedDict(
    '_Food',
    {
        'Use Time': str,
        'Effect Type': str,
        'Max Resource': str,
        'Stimulator Buffs': str,
        ' Health Effects': str,
        'Removes Effects': str,
    },
    total=False,
)


class Food(_Food, ItemBase, Cell):
    pass
