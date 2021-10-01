from Graph import Graph as Graph
from Data_generator import Data_generator as DG

"""
Class used for comparing performance between brute force
and position tracking solution.
"""

n = 15

title_d11 = "2D Brute Force vs Map solution"
title_d12 = "3D Brute Force vs Map solution"

x = list(range(1,n + 1))
y_d11_brute = DG.get_Data_Points(n, 2)
y_d12_brute = DG.get_Data_Points(n, 3)
y_d11_map = DG.get_Data_Points(n, 1)
y_d12_map = DG.get_Data_Points(n, 2)

Graph.draw(x, y_d11_brute, y_d11_map, title_d11)
Graph.draw(x, y_d12_brute, y_d12_map, title_d12)
