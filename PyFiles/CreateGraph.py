from PyFiles.Graph import MyGraph


# Class to create a graph with given number of rows and column of the grid
class createGraph:
    g = None
    rows = None
    columns = None

    def __init__(self, rows, cols):
        self.g = MyGraph()
        self.rows = rows
        self.columns = cols
        # add all nodes
        self.add_all_nodes(self.g)

        # add all  the edgs
        self.add_all_edges(self.g)

    #  Add all nodes of the Graph g.
    def add_all_nodes(self, g):
        print("Creating nodes...")
        for row in range(self.rows):
            for col in range(self.columns):
                g.add_node(str(row) + str(col))

        print("Nodes Created.")

    # Add all the edges of the Graph g
    def add_all_edges(self, g):
        print("Inserting edges...")
        #  adding all horizontal edges (adding row wise)
        for i in range(self.rows):
            for j in range(self.columns - 1):
                g.add_edge(fromNode=str(i) + str(j), toNode=str(i) + str(j + 1), value=1)

        #  adding all vertical edges (adding column wise)
        for j in range(self.columns):
            for i in range(self.rows - 1):
                g.add_edge(fromNode=str(i) + str(j), toNode=str(i + 1) + str(j), value=1)

        print("Edges inserted.")

    # function to get all the nodes created
    def get_all_nodes(self):
        return self.g.getAllEdges()

    # function to get the distance between two nodes
    def get_distance(self, fNode, tNode):
        return self.g.getDistance(fromNode=fNode, toNode=tNode)

    # function to get all the edges of the given node
    def get_edges(self, fNode):
        return self.g.getEdges(fromNode=fNode)

    # get the graph created
    def getGraph(self):
        return self.g
