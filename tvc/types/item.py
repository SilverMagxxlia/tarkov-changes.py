from typing import List, TypedDict

Item = TypedDict(
    'Item',
    {
        'Name': str,
        'Item ID': str,
        'props': List[str],
    }
)
