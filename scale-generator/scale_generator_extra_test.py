import pytest

from scale_generator import (
    _enharmonic_complement,
    _uses_flats,
)

enharmonic_complement_test_data = [
    ('C', 'C'),
    ('C#', 'Db'),
    ('Db', 'C#'),
    ('Ab', 'G#'),
]

@pytest.mark.parametrize("note, expected", enharmonic_complement_test_data)
def test__enharmonic_complement(note, expected):
    assert expected == _enharmonic_complement(note)

uses_flats_true_test_data = [
    ("F minor", 'F', "MmMMmMM"),
    ("F major", 'F', "MMmMMMm"),
    ("G locrian", 'G', "mMMmMMM"),
    ("D♭ hexatonic", 'Db', "MMMMMM"),
    ("D harmonic minor", 'D', "MmMMmAm"),
    ("E♭ mixolydian", 'Eb', "MMmMMmM"),
]

uses_flats_false_test_data = [
    ("A lydian", 'A', "MMMmMMm"),
    ("F♯ major", 'F#', "MMmMMMm"),
    ("A pentatonic", 'A', "MMAMA"),
    ("C octatonic", 'C', "MmMmMmMm"),
    ("G enigmatic", 'G', "mAMMMmm"),
    ("D dorian", 'D', "MmMMMmM"),
]

@pytest.mark.parametrize("name, tonic, intervals", uses_flats_true_test_data)
def test__uses_flats_true(name, tonic, intervals):
    # name just helpful for debugging purposes
    assert _uses_flats(tonic, intervals)

@pytest.mark.parametrize("name, tonic, intervals", uses_flats_false_test_data)
def test__uses_flats_false(name, tonic, intervals):
    # name just helpful for debugging purposes
    assert not _uses_flats(tonic, intervals)
