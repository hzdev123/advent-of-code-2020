from Day_4 import Day_4 as D4
from Day_4_1_check import Day_4_1_check as d1
from Day_4_2_check import Day_4_2_check as d2
from Passport_check import Passport_check as PC

def test_day_4_task_config():
    ans = [
        208,
        167
    ]
    FILE = 'data/aoc_2020_day_4_data_task.txt'
    with open(FILE) as f:
        lines = [line.strip() for line in f]

    for idx, pass_check in enumerate(PC.__subclasses__()):
        assert D4.get_nbr_of_valid_passports(pass_check.check_passport, lines) == ans[idx]
