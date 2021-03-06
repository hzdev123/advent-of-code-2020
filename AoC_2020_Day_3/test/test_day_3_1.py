from src.Day_3 import Day_3 as D3

def test_example_config():
    file = 'data/aoc_2020_day_3_data_example.txt'
    assert get_nbr_trees_encountered(file) == 7

def test_task_config():
    file = 'data/aoc_2020_day_3_data_task.txt'
    assert get_nbr_trees_encountered(file) == 148

def get_nbr_trees_encountered(file):
    with open(file) as f:
        lines = [line.strip() for line in f]

    return D3.get_nbr_trees_encountered(lines)
