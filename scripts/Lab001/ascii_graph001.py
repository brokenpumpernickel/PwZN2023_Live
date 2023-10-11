from ascii_graph import Pyasciigraph
from ascii_graph import colors

import collections
from _collections_abc import Iterable 
collections.Iterable = Iterable


data = [('Opcja 1', 30.0, colors.Red), ('Opcja 2', 50, colors.Gre), ('Opcja 3', 70, colors.BBlu), ('Opcja 4', 10, colors.Yel)]

graph = Pyasciigraph()

for line in graph.graph('Wyniki', data):
    print(line)