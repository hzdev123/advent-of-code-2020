
class Day_1_2:
    """
    Helper class for solving advent of code 2020 day 1 part 2
    """

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
        tracer_0 = 0    # tracer: tracks where in list we are.
                        #         Avoid starting over and doing duplicated addition

        for nbr_1 in numbers:
            tracer_0 = tracer_0 + 1
            tracer_1 = tracer_0
            for idx_2 in range(tracer_0, len(numbers) - 1):
                nbr_2 = numbers[idx_2]
                tracer_1 = tracer_1 + 1
                for idx_3 in range(tracer_1, len(numbers)):
                    nbr_3 = numbers[idx_3]
                    if nbr_1 + nbr_2 + nbr_3 == total:
                        return nbr_1 * nbr_2 * nbr_3
        print("List does not contain three entries where sum is: %s" % (total))
