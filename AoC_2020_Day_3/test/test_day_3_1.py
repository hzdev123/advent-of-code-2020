from src.Day_3_1 import Day_3_1 as D31

def test_small_input():
    file = 'data/aoc_2020_day_3_1_data_example.txt'
    assert get_nbr_trees_encountered(file) == 7

def test_large_input():
    file = 'data/aoc_2020_day_3_1_data_task.txt'
    assert get_nbr_trees_encountered(file) == 148

def get_nbr_trees_encountered(file):
    with open(file) as f:
        lines = [line.strip() for line in f]

    return D31.get_nbr_trees_encountered(lines)
