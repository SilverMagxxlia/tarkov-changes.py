from typing import TypedDict

from .cell import Cell
from .item import ItemBase

_Headphone = TypedDict(
    '_HeadPhone',
    {
        'Blocks Earpiece': str,
        'Blocks Eyewear': str,
        'Blocks Headwear': str,
        'Blocks Face Cover': str,
        'Distortion': str,
        'Compressor Treshold': str,
        'Compressor Attack': str,
        'Compressor Release': str,
        'Compressor Gain': str,
        'Cutoff Frequency': str,
        'Resonance': str,
        'Compressor Volume': str,
        'Ambient Volume': str,
        'Dry Volume': str,
        'Can be sold on flea market': str,
    }
)


class Headphone(_Headphone, ItemBase, Cell):
    pass
