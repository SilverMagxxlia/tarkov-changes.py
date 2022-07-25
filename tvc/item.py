from __future__ import annotations

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .types.item import Item as ItemPayload

__all__ = ('Item',)


class Item:

    def __init__(self, payload: ItemPayload) -> None:
        self.name: str = payload['Name']
        self.id: str = payload['Item ID']

        self._update(payload)

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other: Item) -> bool:
        return isinstance(other, Item) and self.id == other.id

    def __ne__(self, other: Item) -> bool:
        return not self.__eq__(other)

    def __repr__(self) -> str:
        attrs = (
            ('id', self.id),
            ('name', self.name),
        )

        joined = ' '.join('%s=%r' % t for t in attrs)
        return f'<{self.__class__.__name__} {joined}>'

    def _update(self, data: ItemPayload) -> None:
        self.props: List[str] = list(data['props'])
