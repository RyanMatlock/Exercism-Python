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

def _is_flat(note: str) -> bool:
    """Return True if note is flat."""
    return len(note) == 2 and (note[-1] == 'b' or note[-1] == '♭')

def _is_natural(note: str) -> bool:
    """Return True if note is natural (i.e. not sharp or flat)."""
    return len(note) == 1

def _is_sharp(note: str) -> bool:
    """Return True if note is sharp."""
    return len(note) == 2 and (note[-1] == '#' or note[-1] == '♯')

_sharp_flat = {}
for sharp, flat in zip(_const.SHARP_SCALE, _const.FLAT_SCALE):
    _sharp_flat[sharp] = flat

_flat_sharp = {}
for sharp, flat in zip(_const.SHARP_SCALE, _const.FLAT_SCALE):
    _flat_sharp[flat] = sharp

def _enharmonic_complement(note: str) -> str:
    """Return the sharp/flat version of a flat/sharp note."""
    return note if _is_natural(note) else \
        _sharp_flat[note] if _is_sharp(note) else \
        _flat_sharp[note]

def _uses_flats(tonic: str, intervals: str) -> bool:
    """Return True if a scale uses flats instead of sharps.

    See https://en.wikipedia.org/wiki/Key_signature#Major_scale_structure"""
    match (tonic, list(intervals)):
        case 'F', _:
            return True
        case tonic, _ if _is_flat(tonic):
            return True
        # dorian + octatonic kludge
        case _, intervals if intervals == list("MmMMMmM") \
             or intervals == list("MmMmMmMm"):
            return False
        case tonic, ['m', 'M', *rest] | ['M', 'm', *rest] \
             if tonic in ('A', 'D', 'G', 'C'):
            return True
        case other:
            return False


class Scale:
    def __init__(self, tonic: str) -> None:
        self.tonic = tonic.title()  # ensure first char is capitalized
        base_scale = _const.SHARP_SCALE if self.tonic in _const.SHARP_SCALE \
            and self.tonic in _const.CONVENTIONAL_SHARP_SCALES \
            else _const.FLAT_SCALE
        root_index = base_scale.index(self.tonic)
        self.scale = [None for _ in range(_const.SCALE_LEN)]
        for i, _ in enumerate(self.scale):
            self.scale[i] = base_scale[(i + root_index) % _const.SCALE_LEN]

    def chromatic(self) -> List[str]:
        """Return all of the ordered notes of the scale."""
        return self.scale

    def interval(self, intervals: str) -> List[str]:
        """Return the scale starting at the tonic for a given interval."""
        use_sharps = not _uses_flats(self.tonic, intervals)

        mode = [self.tonic]
        index = 0
        for interval in intervals:
            index += 1 if interval == "m" else \
                2 if interval == "M" else 3  # nested ternary
            note = self.scale[index % _const.SCALE_LEN]
            mode.append(
                note if use_sharps or _is_flat(note) \
                else _enharmonic_complement(note)
            )
        return mode
