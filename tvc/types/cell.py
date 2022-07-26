from typing import TypedDict

Cell = TypedDict(
    'Cell',
    {
        'Cell Height': str,
        'Cell Width': str,
        'Item Weight': str,
        'Max Stack Size': str,
        'Discard Limit': str,
    }
)
