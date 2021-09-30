
class Day_1_2:
    """
    Helper class for solving advent of code 2020 day 1 part 2
    """

    @staticmethod
    def get_three_entries_product(numbers, total):
        """
        Returns the product of three list entries where the sum is total

        Parameters
        ----------
        numbers : list
            list of integers
        total : integer
            the sum which the three list entries should have

        Returns
        -------
        int
            The product of the three list entries whose sum is total

        """
        complememts = {}
        for nbr in numbers:
            complement = total - nbr
            complememts[complement] = ""

        for nbr_1 in numbers:
            for nbr_2 in numbers:
                if nbr_1 + nbr_2 in complememts:
                    return nbr_1 * nbr_2 * (total - nbr_1 - nbr_2)

        print("List does not contain three entries where sum is: %s" % (total))
