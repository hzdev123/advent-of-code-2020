from src.Day_1_1 import Day_1_1 as D11

def test_example_config():
    file = 'data/aoc_2020_day_1_data_example.txt'
    assert get_two_entries_product(file) == 514579

def test_task_config():
    file = 'data/aoc_2020_day_1_data_task.txt'
    assert get_two_entries_product(file) == 414816

def get_two_entries_product(file):
    total = 2020
    with open(file) as f:
        numbers = [int(line.strip()) for line in f]

    return D11.get_two_entries_product(numbers, total)
