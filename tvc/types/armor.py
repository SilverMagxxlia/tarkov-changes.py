from typing import TypedDict

Armor = TypedDict(
    'Armor',
    {
        'Name': str,
        'Item ID': str,
        'Armor Class': str,
        'Materials': str,
        'Protection Zones': str,
        'Max Durability': str,
        'Effective Durability': float,
        'Movement Speed Penalty': str,
        'Turn Speed Penalty': str,
        'Ergonomics Penalty': str,
        'Blunt Throughput': str,
        'Repair Cost': str,
        'Cell Height': str,
        'Cell Width': str,
        'Item Weight': str,
        'Max Stack Size': str,
        'Can be sold on flea market': str,
        'Discard Limit': str,
    }
)
