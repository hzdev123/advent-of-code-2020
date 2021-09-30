
class Day_1_1:
    """
    Helper class for solving advent of code 2020 day 1 part 1
    """

    @staticmethod
    def get_two_entries_product(numbers, total):
        """
        Returns the product of two list entries where the sum is total

        Parameters
        ----------
        numbers : list
            list of integers
        total : integer
            the sum which the two list entries should have

        Returns
        -------
        int
            The product of the two list entries whose sum is total

        """
        complememts = {}
        for nbr in numbers:
            complement = total - nbr
            complememts[complement] = ""

        for nbr in numbers:
            if nbr in complememts:
                return nbr * (total - nbr)
        print("List does not contain two entries where sum is: %s" % (total))
