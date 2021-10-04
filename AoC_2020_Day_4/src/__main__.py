import re
from Day_4 import Day_4 as D4
from Passport_check import Passport_check as PC

'''
https://adventofcode.com/2020/day/4
'''
print("Starting advent of code 2020 day 4")

FILE = 'data/aoc_2020_day_4_data_task.txt'
with open(FILE) as f:
    lines = [line.strip() for line in f]

print("Advent of code 2020 day 4-1 solved: %s" % \
    D4.get_nbr_of_valid_passports(PC.valid, lines))
print("Advent of code 2020 day 4-2 solved: %s" % \
    D4.get_nbr_of_valid_passports(PC.is_valid_fields, lines))
