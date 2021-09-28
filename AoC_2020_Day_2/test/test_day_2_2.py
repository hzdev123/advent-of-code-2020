from src.Day_2_2 import Day_2_2 as D22

def test_small_input():
    file = 'data/aoc_2020_day_2_data_example.txt'
    assert get_nbr_of_valid_password_new(file) == 1

def test_large_input():
    file = 'data/aoc_2020_day_2_data_task.txt'
    assert get_nbr_of_valid_password_new(file) == 489

def get_nbr_of_valid_password_new(file):
    with open(file) as f:
        lines = [line.strip() for line in f]

    return D22.get_nbr_of_valid_password_new(lines)
