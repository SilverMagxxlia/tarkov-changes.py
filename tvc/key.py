from __future__ import annotations

from typing import Union, TYPE_CHECKING

from .mixins import Hashable

if TYPE_CHECKING:
    from .types.key import Key as KeyPayload

__all__ = ('Key',)


class Key(Hashable):

    def __init__(self, payload: KeyPayload) -> None:
        self.name: str = payload['Name']
        self.id: str = payload['Item ID']

        self._update(payload)

    def __str__(self) -> str:
        return self.name

    def __int__(self) -> int:
        return self.maximum_usage

    def __eq__(self, other: Key) -> bool:
        return isinstance(other, Key) and self.id == other.id

    def __ne__(self, other: Key) -> bool:
        return not self.__eq__(other)

    def __repr__(self) -> str:
        attrs = (
            ('id', self.id),
            ('name', self.name),
            ('fixed_price', self.fixed_price),
            ('maximum_usage', self.maximum_usage)
        )

        joined = ' '.join('%s=%r' % t for t in attrs)
        return f'<{self.__class__.__name__} {joined}>'

    @property
    def image_url(self):
        return f'https://tarkov-changes.com/img/items/128/{self.id}.png'

    def _update(self, data: KeyPayload) -> None:
        fixed_price: Union[int, None] = data['Fixed Price']

        if fixed_price is None:
            fixed_price = 0

        self.fixed_price = fixed_price
        self.unlootable: bool = 'true' == data['Unlootable']
        self.discarding_block: bool = 'true' == data['Discarding Block']
        self.maximum_usage: int = int(data['MaximumNumber Of Usage'] or 0)
        self.cell_height: int = int(data['Cell Height'])
        self.cell_width: int = int(data['Cell Width'])
        self.max_stack_size: int = int(data['Max Stack Size'])
        self.discard_limit: int = int(data['Discard Limit'])
