"""scale_generator.py"""

from typing import List
from types import SimpleNamespace

_const = SimpleNamespace()

_const.SHARP_SCALE = [
    "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"
]

_const.FLAT_SCALE = [
    "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"
]

_const.CONVENTIONAL_SHARP_SCALES = ["C", "G", "D", "A", "E", "B", "F#"]

_const.SCALE_LEN = len(_const.SHARP_SCALE)
assert _const.SCALE_LEN == len(_const.FLAT_SCALE)

_sharp_flat = {}
for sharp, flat in zip(_const.SHARP_SCALE, _const.FLAT_SCALE):
    _sharp_flat[sharp] = flat

def _sharp_to_flat(sharp_note: str) -> str:
    """Return the flat version of sharp_note."""
    return _sharp_flat[sharp_note]


class Scale:
    def __init__(self, tonic: str) -> None:
        tonic = tonic.title()  # ensure first char is capitalized
        base_scale = _const.SHARP_SCALE if tonic in _const.SHARP_SCALE and \
            tonic in _const.CONVENTIONAL_SHARP_SCALES else _const.FLAT_SCALE
        root_index = base_scale.index(tonic)
        self.scale = [None for _ in range(_const.SCALE_LEN)]
        for i, _ in enumerate(self.scale):
            self.scale[i] = base_scale[(i + root_index) % _const.SCALE_LEN]

    def chromatic(self) -> List[str]:
        """Return all of the ordered notes of the scale."""
        return self.scale

    def interval(self, intervals: str) -> List[str]:
        use_sharps = self.scale[0] not in _const.FLAT_SCALE and \
            True  # struggling with the conditions for sharp/flat notes

        index = 0
        mode = [self.scale[index]]
        for interval in intervals:
            index += 1 if interval == "m" else \
                2 if interval == "M" else 3  # nested ternary
            note = self.scale[index % _const.SCALE_LEN]
            mode.append(
                note if use_sharps else _sharp_to_flat(note)
            )
        return mode
