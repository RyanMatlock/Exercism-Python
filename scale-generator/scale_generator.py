"""scale_generator.py"""

from typing import List

SHARP_SCALE = [
    "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"
]

FLAT_SCALE = [
    "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"
]

CONVENTIONAL_SHARP_SCALES = ["C", "G", "D", "A", "E", "B", "F#"]

SCALE_LEN = len(SHARP_SCALE)
assert SCALE_LEN == len(FLAT_SCALE)


class Scale:
    def __init__(self, tonic: str) -> None:
        tonic = tonic.title()  # ensure first char is capitalized
        base_scale = SHARP_SCALE if tonic in SHARP_SCALE and \
            tonic in CONVENTIONAL_SHARP_SCALES else FLAT_SCALE
        root_index = base_scale.index(tonic)
        self.scale = [None for _ in range(SCALE_LEN)]
        for i, _ in enumerate(self.scale):
            self.scale[i] = base_scale[(i + root_index) % SCALE_LEN]

    def chromatic(self) -> List[str]:
        return self.scale

    def interval(self, intervals: str) -> List[str]:
        index = 0
        mode = [self.scale[index]]
        for interval in intervals:
            index += 1 if interval == "m" else \
                2 if interval == "M" else 3  # nested ternary
            mode.append(self.scale[index % SCALE_LEN])
        return mode
