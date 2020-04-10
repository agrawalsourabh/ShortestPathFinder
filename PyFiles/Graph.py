from collections import defaultdict

# Class Graph used by the CreateGraph class
class MyGraph:
    nodes = set()
    edges = defaultdict(list)
    distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, fromNode, toNode, value):
        self.edges[fromNode].append(toNode)
        self.edges[toNode].append(fromNode)
        self.distances[(fromNode, toNode)] = value
        self.distances[(toNode, fromNode)] = value

    def getNodes(self):
        return self.nodes

    def getAllEdges(self):
        return self.edges

    def displayDistances(self):
        print(self.distances)

    def getDistance(self, fromNode, toNode):
        return self.distances[(fromNode, toNode)]

    def getEdges(self, fromNode):
        return self.edges[fromNode]

