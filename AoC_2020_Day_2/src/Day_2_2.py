import re

class Day_2_2:
    """
    Helper class for solving advent of code 2020 day 2 part 2
    """

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
        pos_one_regex = "^(\d+)-\d+ \S: \S+$"
        pos_two_regex = "^\d+-(\d+) \S: \S+$"
        token_regex = "^\d+-\d+ (\S): \S+$"

        nbr_of_valid_pass = 0
        for line in lines:
            p_one = int(re.sub(pos_one_regex, r"\1", line)) - 1
            p_two = int(re.sub(pos_two_regex, r"\1", line)) - 1
            tok = re.sub(token_regex, r"\1", line)
            pw = line.split(":")[1].strip()

            if (pw[p_one] == tok and pw[p_two] != tok) or \
                (pw[p_one] != tok and pw[p_two] == tok):
                nbr_of_valid_pass = nbr_of_valid_pass + 1

        return nbr_of_valid_pass
