from src.Day_2_1 import Day_2_1 as D21

def test_small_input():
    file = 'data/aoc_2020_day_2_1_data_small.txt'
    assert get_nbr_of_valid_password(file) == 2

def test_large_input():
    file = 'data/aoc_2020_day_2_1_data_large.txt'
    assert get_nbr_of_valid_password(file) == 538

def get_nbr_of_valid_password(file):
    with open(file) as f:
        lines = [line.strip() for line in f]

    return D21.get_nbr_of_valid_password(lines)
