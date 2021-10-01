class Data_generator:
    """
    Helper class for generating number of iterations given number of list entries in data set
    """

    @staticmethod
    def get_Data_Points(n, exp):
        """
        Returns a list over the number of iterations from 1 to n + 1

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
