from src.Day_1_2 import Day_1_2 as D12

def test_example_config():
    file = 'data/aoc_2020_day_1_data_example.txt'
    assert get_three_entries_product(file) == 241861950

def test_task_config():
    file = 'data/aoc_2020_day_1_data_task.txt'
    assert get_three_entries_product(file) == 161109702

def get_three_entries_product(file):
    total = 2020
    with open(file) as f:
        numbers = [int(line.strip()) for line in f]

    return D12.get_three_entries_product(numbers, total)
