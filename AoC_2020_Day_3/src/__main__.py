from Day_3 import Day_3 as D3

'''
https://adventofcode.com/2020/day/3
'''
print("Starting advent of code 2020 day 3")

FILE = 'data/aoc_2020_day_3_data_task.txt'
with open(FILE) as f:
    lines = [line.strip() for line in f]

print("Advent of code 2020 day 3-1 solved: %s" % D3.get_nbr_trees_encountered(lines))

prod_enc_trees = D3.get_nbr_trees_encountered(lines, 1, 1) \
    * D3.get_nbr_trees_encountered(lines) \
    * D3.get_nbr_trees_encountered(lines, 5, 1) \
    * D3.get_nbr_trees_encountered(lines, 7, 1) \
    * D3.get_nbr_trees_encountered(lines, 1, 2)

print("Advent of code 2020 day 3-2 solved: %s" % prod_enc_trees)
