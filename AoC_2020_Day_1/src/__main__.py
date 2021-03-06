from Day_1_1 import Day_1_1 as D11
from Day_1_2 import Day_1_2 as D12

'''
https://adventofcode.com/2020/day/1
'''

print("Starting advent of code 2020 day 1")

FILE = 'data/aoc_2020_day_1_data_task.txt'
TOTAL = 2020

with open(FILE) as f:
    numbers = [int(line.strip()) for line in f]

print("Advent of code 2020 day 1-1 solved: %s" % D11.get_two_entries_product(numbers, TOTAL))
print("Advent of code 2020 day 1-2 solved: %s" % D12.get_three_entries_product(numbers, TOTAL))
