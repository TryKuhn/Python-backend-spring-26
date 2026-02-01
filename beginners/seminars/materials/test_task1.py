import pytest
from beginners.seminars.materials.task1_sem2 import find_first_occurrence

def test_find_first_occurrence_present():
    # Test case 1: Number is present in the array
    array_len = 5
    search_number = 3
    array_elements = [1, 2, 3, 4, 5]
    assert find_first_occurrence(array_len, search_number, array_elements) == 3

def test_find_first_occurrence_not_present():
    # Test case 2: Number is not present in the array
    array_len = 4
    search_number = 6
    array_elements = [1, 2, 3, 4]
    with pytest.raises(IndexError):
        find_first_occurrence(array_len, search_number, array_elements)

def test_find_first_occurrence_begin():
    # Test case 3: Number is at the beginning of the array
    array_len = 3
    search_number = 1
    array_elements = [1, 2, 3]
    assert find_first_occurrence(array_len, search_number, array_elements) == 1

def test_find_first_occurrence_end():
    # Test case 4: Number is at the end of the array
    array_len = 3
    search_number = 3
    array_elements = [1, 2, 3]
    assert find_first_occurrence(array_len, search_number, array_elements) == 3

def test_find_first_occurrence_negative_numbers():
    # Test case 5: Array with negative numbers
    array_len = 5
    search_number = -2
    array_elements = [-5, -4, -3, -2, -1]
    assert find_first_occurrence(array_len, search_number, array_elements) == 4