import re

class Day_2_1:
    """
    Helper class for solving advent of code 2020 day 2 part 1
    """

    def get_nbr_of_valid_password_old(lines):
        """
        Returns the number of valid password based on password policy

        Parameters
        ----------
        lines : list
            list of password policy and passwords

        Returns
        -------
        int
            The number of valid passwords

        """
        min_regex = "^(\d+)-\d+ \S: \S+$"
        max_regex = "^\d+-(\d+) \S: \S+$"
        token_regex = "^\d+-\d+ (\S): \S+$"

        nbr_of_valid_pass = 0
        for line in lines:
            min_limit = int(re.sub(min_regex, r"\1", line))
            max_limit = int(re.sub(max_regex, r"\1", line))
            token = re.sub(token_regex, r"\1", line)
            password = line.split(":")[1].strip()
            token_in_pass = password.count(token)

            if min_limit <= token_in_pass <= max_limit:
                nbr_of_valid_pass = nbr_of_valid_pass + 1

        return nbr_of_valid_pass
