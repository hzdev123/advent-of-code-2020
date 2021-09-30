class Data_generator:
    """
    Helper class for generating number of iterations given number of list entries in data set
    """

    @staticmethod
    def get_Brute_Data(n, exp):
        """
        Returns a list over the number of iterations from 1 to n + 1

        These data points represent solving day-1 with brute force

        Parameters
        ----------
        n : int
            number of list entries
        exp : int
            the dimension of the data set

        Returns
        -------
        list
            contains the number of iterations from 1 to n + 1

        """
        data = []
        for i in range(1, n + 1):
            data.append(i**exp)
        return data

    @staticmethod
    def get_Day_1_1_Tracked_Data(n):
        """
        Returns a list over the number of iterations from 1 to n + 1

        These data points represent solving day-1-1 while tracking list position

        Parameters
        ----------
        n : int
            number of list entries

        Returns
        -------
        list
            contains the number of iterations from 1 to n + 1

        """
        data = []
        for i in range(1, n + 1):
            data.append(sum(range(1, i)))
        return data

    @staticmethod
    def get_Day_1_2_Tracked_Data(n):
        """
        Returns a list over the number of iterations from 1 to n + 1

        These data points represent solving day-1-2 while tracking list position

        Parameters
        ----------
        n : int
            number of list entries

        Returns
        -------
        list
            contains the number of iterations from 1 to n + 1

        """
        data = []
        prev_sum = 0
        for i in range(1, n + 1):
            if i > 2:
                prev_sum = sum(range(1, i - 1)) + prev_sum
                data.append(prev_sum)
            else:
                data.append(0)
        return data
