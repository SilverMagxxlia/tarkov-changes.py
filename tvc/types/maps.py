from typing import TypedDict

Map = TypedDict(
    'Map',
    {
        'Name': str,
        'Map Enabled': bool,
        'Map Locked': bool,
        'Map Internal Name': str,
        'Avg. Player Level': float,
        'Raid Timer': int,
        'Max Players': float,
        'Min Players': float,
        'Required Player Level': float,
    },
    total=False,
)
