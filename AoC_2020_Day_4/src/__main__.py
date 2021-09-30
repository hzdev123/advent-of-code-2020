from Day_4_1 import Day_4_1 as D41

'''
https://adventofcode.com/2020/day/4
'''
print("Starting advent of code 2020 day 4")

FILE = 'data/aoc_2020_day_4_data_task.txt'
with open(FILE) as f:
    lines = [line.strip() for line in f]

print("Advent of code 2020 day 4-1 solved: %s" % D41.get_nbr_of_valid_passports(lines))
print("Advent of code 2020 day 4-2 solved: %s" % D42.get_nbr_of_valid_passports(lines))
