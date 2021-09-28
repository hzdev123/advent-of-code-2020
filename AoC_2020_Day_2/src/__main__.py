from Day_2_1 import Day_2_1 as D21
from Day_2_2 import Day_2_2 as D22

'''
https://adventofcode.com/2020/day/2
'''

print("Starting advent of code 2020 day 2")

FILE = 'data/aoc_2020_day_2_data_task.txt'
with open(FILE) as f:
    lines = [line.strip() for line in f]

print("Advent of code 2020 day 2-1 solved: %s" % D21.get_nbr_of_valid_password_old(lines))
print("Advent of code 2020 day 2-2 solved: %s" % D22.get_nbr_of_valid_password_new(lines))
