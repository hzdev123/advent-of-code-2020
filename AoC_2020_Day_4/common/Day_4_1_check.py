from Passport_check import Passport_check

class Day_4_1_check(Passport_check):

    @staticmethod
    def check_passport(mandatory_fields, line):
        """
        Only check that the fields are present.
        Does not check field content.

        Parameters
        ----------
        mandatory_fields : list
            list over required fields in passport
        line : str
            string representing the passport

        Returns
        -------
        bool:
            Returns True if all fields are present
        """
        for mandatory_field in mandatory_fields:
            if mandatory_field not in line:
                return False
        return True