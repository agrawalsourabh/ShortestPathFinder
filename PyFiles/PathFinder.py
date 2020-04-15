from .CreateGraph import createGraph
from .Dijsktra import dijsktra
from .AStar import astar



# from Graph_Data.Algorithms import Dijsktra

class PathFinder:
    cGraph = None
    graph = None

    def __init__(self):
        self.cGraph = createGraph(rows=18, cols=50)
        self.graph = self.cGraph.getGraph()

    def find_dijsktra_path(self, initial, endNode):

        return dijsktra(graph=self.graph, initial=initial, endNode=endNode)

    def find_astar_path(self, initial, endNode):
        return astar(graph=self.graph, start_node=initial, end_node=endNode)



# print("Visited: ")
# print(visited)
# print("Path: ")
# print(path)
# print("Path Edge: ")
# print(path_edge)
