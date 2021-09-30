from src.Day_4_1 import Day_4_1 as D41

def test_example_config():
    file = 'data/aoc_2020_day_4_data_example.txt'
    assert get_nbr_of_valid_passports(file) == 2

def test_task_config():
    file = 'data/aoc_2020_day_4_data_task.txt'
    assert get_nbr_of_valid_passports(file) == 208

def get_nbr_of_valid_passports(file):
    with open(file) as f:
        lines = [line.strip() for line in f]

    return D41.get_nbr_of_valid_passports(lines)
