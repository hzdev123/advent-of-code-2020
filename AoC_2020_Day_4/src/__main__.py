#!/usr/bin/python3.9
import sys
import pathlib
COMMON = "common"
if len(sys.argv) > 1:
    COMMON = sys.argv[1]
sys.path.append(str(pathlib.Path().resolve()) + "/" + COMMON)

from Day_4 import Day_4 as D4
from Day_4_1_check import Day_4_1_check
from Day_4_2_check import Day_4_2_check
from Passport_check import Passport_check as PC

'''
https://adventofcode.com/2020/day/4
'''
print("Starting advent of code 2020 day 4")

FILE = 'data/aoc_2020_day_4_data_task.txt'
with open(FILE) as f:
    lines = [line.strip() for line in f]

for idx, pass_check in enumerate(PC.__subclasses__()):
    print("Advent of code 2020 day 4-%s solved: %s" % \
        (idx, \
        D4.get_nbr_of_valid_passports(pass_check.check_passport, lines)))

print("Advent of code 2020 day 4")
