from typing import TypedDict

from .cell import Cell
from .item import ItemBase

_Ammunition = TypedDict(
    '_Ammunition',
    {
        'Caliber': str,
        'Accuracy': str,
        'Recoil': str,
        'Flesh Damage': str,
        'Penetration Power': str,
        'Armor Damage': str,
        'Frag Chance': str,
        'Durability Burn': str,
        'Stamina Burn per Dmg': str,
        'Projectile Speed': str,
        'Misfire Chance': str,
        'Penetration Chance': str,
        'Ricochet Chance': str,
        'Heavy Bleeding Delta': str,
        'Light Bleeding Delta': str,
        'Ballistic Coefficient': str,
        'Item Weight': str,
        'Max Stack Size': str,
        'Discard Limit': str,
    },
    total=False,
)


class Ammunition(_Ammunition, ItemBase, Cell):
    pass
