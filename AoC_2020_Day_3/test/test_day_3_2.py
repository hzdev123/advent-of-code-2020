from src.Day_3 import Day_3 as D3

def test_example_input():
    file = 'data/aoc_2020_day_3_data_example.txt'
    assert get_nbr_trees_encountered(file) == 336

def test_task_input():
    file = 'data/aoc_2020_day_3_data_task.txt'
    assert get_nbr_trees_encountered(file) == 727923200

def get_nbr_trees_encountered(file):
    with open(file) as f:
        lines = [line.strip() for line in f]

    prod_enc_trees = D3.get_nbr_trees_encountered(lines, 1, 1) \
        * D3.get_nbr_trees_encountered(lines) \
        * D3.get_nbr_trees_encountered(lines, 5, 1) \
        * D3.get_nbr_trees_encountered(lines, 7, 1) \
        * D3.get_nbr_trees_encountered(lines, 1, 2)

    return prod_enc_trees
