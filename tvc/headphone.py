from __future__ import annotations

from typing import TYPE_CHECKING

from .mixins import Hashable

if TYPE_CHECKING:
    from .types.headphone import Headphone as HeadphonePayload

__all__ = ('Headphone',)


class Headphone(Hashable):

    def __init__(self, payload: HeadphonePayload) -> None:
        self.name: str = payload['Name']
        self.id: str = payload['Item ID']

        self._update(payload)

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other: Headphone) -> bool:
        return isinstance(other, Headphone) and self.id == other.id

    def __ne__(self, other: Headphone) -> bool:
        return not self.__eq__(other)

    def _update(self, data: HeadphonePayload) -> None:
        self.block_earpiece: bool = 'true' == data['Blocks Earpiece']
        self.block_eyewear: bool = 'true' == data['Blocks Eyewear']
        self.block_headwear: bool = 'true' == data['Blocks Headwear']
        self.block_face_cover: bool = 'true' == data['Blocks Face Cover']
        self.distortion: float = float(data['Distortion'])

        self.compressor_treshold: int = int(data['Compressor Treshold'])
        self.compressor_attack: int = int(data['Compressor Treshold'])
        self.compressor_release: int = int(data['Compressor Release'])
        self.compressor_gain: int = int(data['Compressor Gain'])

        self.cutoff_ferquency: int = int(data['Cutoff Frequency'])
        self.resonance: int = int(data['Resonance'])

        self.compressor_volume: int = int(data['Compressor Volume'])
        self.ambient_volume: int = int(data['Ambient Volume'])
        self.dry_volume: int = int(data['Dry Volume'])

        self.cell_height: int = int(data['Cell Height'])
        self.width: int = int(data['Cell Width'])
        self.weight: float = float(data['Item Weight'])
        self.banned_on_flea: bool = data['Can be sold on flea market'] == 'false'
        self.max_stack_size: int = int(data['Max Stack Size'])
        self.discard_limit: int = int(data['Discard Limit'])
