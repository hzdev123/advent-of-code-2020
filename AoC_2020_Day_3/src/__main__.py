from Day_3_1 import Day_3_1 as D31

'''
https://adventofcode.com/2020/day/3
'''
print("Starting advent of code 2020 day 3")

FILE = 'data/aoc_2020_day_3_data_task.txt'
with open(FILE) as f:
    lines = [line.strip() for line in f]

print("Advent of code 2020 day 3 solved: %s" % D31.get_nbr_trees_encountered(lines))
