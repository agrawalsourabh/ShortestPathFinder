from .CreateGraph import createGraph
from .Dijsktra import dijsktra


# from Graph_Data.Algorithms import Dijsktra

class PathFinder:
    cGraph = None
    graph = None

    def __init__(self):
        self.cGraph = createGraph(rows=22, cols=50)
        self.graph = self.cGraph.getGraph()

    def find_dijsktra_path(self, initial, endNode):


        # print("Visited:", visited)
        # print("Path:", path)
        # print("Path with Edged:", path_edge)

        return dijsktra(graph=self.graph, initial=initial, endNode=endNode)


# print("Visited: ")
# print(visited)
# print("Path: ")
# print(path)
# print("Path Edge: ")
# print(path_edge)
