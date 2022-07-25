from typing import List, TypedDict

ItemBase = TypedDict(
    'ItemBase',
    {
        'Name': str,
        'Item ID': str,
    },
    total=False,
)


class Item(ItemBase):
    props: List[str]
