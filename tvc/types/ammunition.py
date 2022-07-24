from typing import TypedDict

Ammunition = TypedDict(
    'Ammunition',
    {
        'Name': str,
        'Caliber': str,
        'Accuracy': str,
        'Recoil': str,
        'Item ID': str,
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
        'Cell Height': str,
        'Cell Width': str,
        'Item Weight': str,
        'Max Stack Size': str,
        'Discard Limit': str,
    }
)