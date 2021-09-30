import re

class Day_2_2:
    """
    Helper class for solving advent of code 2020 day 2 part 2
    """

    @staticmethod
    def get_nbr_of_valid_password_new(lines):
        """
        Returns the number of valid password based on password policy
        See README 2.2 Day 2-2

        Parameters
        ----------
        lines : list
            list of password policy and passwords

        Returns
        -------
        int
            The number of valid passwords

        """
        all_regex = "^(\d+)-(\d+) (\S): (\S+)$"

        nbr_of_valid_pass = 0
        for line in lines:
            p_one = int(re.sub(all_regex, r"\1", line)) - 1
            p_two = int(re.sub(all_regex, r"\2", line)) - 1
            tok = re.sub(all_regex, r"\3", line)
            pw = re.sub(all_regex, r"\4", line)

            if (pw[p_one] == tok and pw[p_two] != tok) or \
                (pw[p_one] != tok and pw[p_two] == tok):
                nbr_of_valid_pass = nbr_of_valid_pass + 1

        return nbr_of_valid_pass
