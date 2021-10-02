import re
from Day_4_1 import Day_4_1 as D41
from Day_4_2 import Day_4_2 as D42

def is_valid_fields(mandatory_fields, line):
    BYR = ' byr:'
    IYR = ' iyr:'
    EYR = ' eyr:'
    HGT = ' hgt:'
    HCL = ' hcl:'
    ECL = ' ecl:'
    PID = ' pid:'
    for f in mandatory_fields:
        field_regex = ".*%s(\S+)\s?.*" % f
        f_val = re.sub(field_regex, r"\1", line)

        if f == BYR and not 1920 <= int(f_val) <= 2002:
            return False
        elif f == IYR and not 2010 <= int(f_val) <= 2020:
            return False
        elif f == EYR and not 2020 <= int(f_val) <= 2030:
            return False
        elif f == HGT and 'cm' in f_val and not 150 <= int(f_val.replace("cm", "")) <= 193:
            return False
        elif f == HGT and 'in' in f_val and not 59 <= int(f_val.replace("in", "")) <= 76:
            return False
        elif f == HCL and re.search("^#[0-9a-f]{6}$", f_val) is None:
            return False
        elif f == ECL and re.search("^(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)$", f_val) is None:
            return False
        elif f == PID and re.search("^[0-9]{9}$", f_val) is None:
            return False

    return True

'''
https://adventofcode.com/2020/day/4
'''
print("Starting advent of code 2020 day 4")

FILE = 'data/aoc_2020_day_4_data_example.txt'
with open(FILE) as f:
    lines = [line.strip() for line in f]

print("Advent of code 2020 day 4-1 solved: %s" % \
    D41.get_nbr_of_valid_passports(lines))
print("Advent of code 2020 day 4-2 solved: %s" % \
        D42.get_nbr_of_valid_passports(is_valid_fields, lines))
