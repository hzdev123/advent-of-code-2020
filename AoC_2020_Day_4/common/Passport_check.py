from abc import ABC, abstractmethod

class Passport_check(ABC):
    """
    Abstract class for handling passport validity checking
    """

    @abstractmethod
    def check_passport(mandatory_fields, line):
        """
        Checks the validity of a passport

        Parameters
        ----------
        mandatory_fields : list
            list over required fields in passport
        line : str
            string representing the passport

        Returns
        -------
        """
        pass
