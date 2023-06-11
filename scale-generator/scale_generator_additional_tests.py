import pytest

from scale_generator import _enharmonic_complement

enharmonic_complement_test_data = [
    ('C', 'C'),
    ('C#', 'Db'),
    ('Db', 'C#'),
    ('Ab', 'G#'),
]

@pytest.mark.parametrize("note, expected", enharmonic_complement_test_data)
def test__enharmonic_complement(note, expected):
    assert expected == _enharmonic_complement(note)
