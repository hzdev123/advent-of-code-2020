import re

class Day_4:
    """
    Helper class for solving advent of code 2020 day 4 part 2
    """

    @staticmethod
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
        nbr_of_valid_passports = 0
        for line in lines:
            if len(line) == 0:
                if func(mandatory_fields, prev_str):
                    nbr_of_valid_passports = nbr_of_valid_passports + 1

                prev_str = ""
            else:
                prev_str += " " + line

        if func(mandatory_fields, prev_str):
            nbr_of_valid_passports = nbr_of_valid_passports + 1

        return nbr_of_valid_passports
