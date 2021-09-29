
class Day_3_1:
    """
    Helper class for solving advent of code 2020 day 3 part 1
    """

    def get_nbr_trees_encountered(lines, horizontal = 3, vertical = 1):
        """
        Returns the number of trees encountered along the slope

        Parameters
        ----------
        lines : list
            list describing the topology

        horizontal : int
            number of steps to move to the right for each slope

        vertical : int
            number of steps to move down for each slope

        Returns
        -------
        int
            The number of trees encountered

        """
        current_pos = 0
        area_lenght = len(lines[0])
        nbr_of_trees = 0
        for idx in range(vertical, len(lines), vertical):
            current_pos = current_pos + horizontal
            current_char = lines[idx][current_pos % area_lenght]

            if current_char == '#':
                nbr_of_trees = nbr_of_trees + 1

        return nbr_of_trees
