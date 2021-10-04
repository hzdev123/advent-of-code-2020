from src.Day_4 import Day_4 as D4

def valid(mandatory_fields, line):
    for mandatory_field in mandatory_fields:
        if mandatory_field not in line:
            return False
    return True

def test_example_config():
    file = 'data/aoc_2020_day_4_data_example.txt'
    assert get_nbr_of_valid_passports(file) == 2

def test_task_config():
    file = 'data/aoc_2020_day_4_data_task.txt'
    assert get_nbr_of_valid_passports(file) == 208

def get_nbr_of_valid_passports(file):
    with open(file) as f:
        lines = [line.strip() for line in f]

    return D4.get_nbr_of_valid_passports(valid, lines)
