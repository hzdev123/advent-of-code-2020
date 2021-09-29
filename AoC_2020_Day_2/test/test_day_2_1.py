from src.Day_2_1 import Day_2_1 as D21

def test_example_config():
    file = 'data/aoc_2020_day_2_data_example.txt'
    assert get_nbr_of_valid_password_old(file) == 2

def test_task_config():
    file = 'data/aoc_2020_day_2_data_task.txt'
    assert get_nbr_of_valid_password_old(file) == 538

def get_nbr_of_valid_password_old(file):
    with open(file) as f:
        lines = [line.strip() for line in f]

    return D21.get_nbr_of_valid_password_old(lines)
