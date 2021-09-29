from Graph import Graph as Graph
from Data_generator import Data_generator as DG

"""
Class used for comparing performance between brute force
and position tracking solution.
"""


n = 500

title_d11 = "2D Brute Force vs Position Tracking"
title_d12 = "3D Brute Force vs Position Tracking"

x = list(range(1,n + 1))
y_d11_brute = DG.get_Brute_Data(n, 2)
y_d12_brute = DG.get_Brute_Data(n, 3)
y_d11_ok = DG.get_Day_1_1_Tracked_Data(n)
y_d12_ok = DG.get_Day_1_2_Tracked_Data(n)

Graph.compare(x, y_d11_brute, y_d11_ok, title_d11)
Graph.compare(x, y_d12_brute, y_d12_ok, title_d12)
