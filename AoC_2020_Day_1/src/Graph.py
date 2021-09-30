import matplotlib.pyplot as plt

class Graph:
	"""
    Class for drawing graphs
    """

	@staticmethod
	def draw(x, y1, y2, title):
		"""
		Draws a graph where two curves are compared

        Parameters
        ----------
        x : list
            list of values along the x-axis
        y1 : list
			list of values along the y-axis
		y2 : list
			list of values along the y-axis
		title : str
		    graph title
        Returns
        -------
			None
        """
		plt.plot(x, y1)
		plt.plot(x, y2)
		plt.xlabel('Number of list entries')
		plt.ylabel('Amount of iterations')
		plt.title(title)
		plt.show()
