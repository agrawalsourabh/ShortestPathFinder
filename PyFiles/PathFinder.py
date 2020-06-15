from .CreateGraph import createGraph
from .Dijsktra import dijsktra
from .AStar import astar



# from Graph_Data.Algorithms import Dijsktra

class PathFinder:
    cGraph = None
    graph = None
    rows = None
    columns = None
   

    def set_rows(self, rows):
        self.rows = rows

    def set_columns(self, columns):
        self.columns = columns

    def get_rows(self):
        return  self.rows
    
    def get_columns(self):
        return self.columns

    def createGraph(self):
        self.cGraph = createGraph(rows=self.get_rows(), cols=self.get_columns())
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
