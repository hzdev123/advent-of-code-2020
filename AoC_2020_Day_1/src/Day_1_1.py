
class Day_1_1:
    """
    Helper class for solving advent of code 2020 day 1 part 1
    """

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
        tracer = 0      # tracer: tracks where in list we are.
                        #         Avoid starting over and doing duplicated addition
        for nbr_1 in numbers:
            tracer = tracer + 1
            for idx in range(tracer, len(numbers)):
                nbr_2 = numbers[idx]
                if nbr_1 + nbr_2 == total:
                    return nbr_1 * nbr_2 # 18578
        print("List does not contain two entries where sum is: %s" % (total))
