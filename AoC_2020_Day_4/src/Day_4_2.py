import re

class Day_4_2:
    """
    Helper class for solving advent of code 2020 day 4 part 2
    """

    def get_nbr_of_valid_passports(func, lines):
        """
        Returns the number of trees encountered along the slope

        Parameters
        ----------
        func : function
            defines a valid passport
        lines : list
            list of passports

        Returns
        -------
        int
            The number of valid passports

        """
        mandatory_fields = [
            ' byr:',
            ' iyr:',
            ' eyr:',
            ' hgt:',
            ' hcl:',
            ' ecl:',
            ' pid:'
        ]

        prev_str = ""
        processed_lines = []
        for line in lines:
            if len(line) == 0:
                processed_lines.append(" " + prev_str)
                prev_str = ""
            else:
                prev_str += " " + line
        processed_lines.append(" " + prev_str)

        nbr_of_valid_passports = 0
        for line in processed_lines:
            for idx, field in enumerate(mandatory_fields):
                if field not in line:
                    break
                if idx == len(mandatory_fields) - 1 and func(mandatory_fields, line):
                    nbr_of_valid_passports = nbr_of_valid_passports + 1

        return nbr_of_valid_passports
