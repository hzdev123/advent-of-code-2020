from src.Day_1_1 import Day_1_1 as D11

def test_small_input():
    file = 'data/aoc_2020_day_1_1_data_small.txt'
    assert get_product(file) == 514579

def test_large_input():
    file = 'data/aoc_2020_day_1_1_data_large.txt'
    assert get_product(file) == 485739

def get_product(file):
    total = 2020
    with open(file) as f:
        numbers = [int(line.strip()) for line in f]

    return D11.find_product(numbers, total)
