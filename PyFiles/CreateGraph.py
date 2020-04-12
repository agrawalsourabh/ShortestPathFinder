from .Graph import MyGraph


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
        id = 0
        for row in range(self.rows):
            for col in range(self.columns):
                g.add_node(str(id))
                id = id + 1

        print("Nodes Created.")

    # Add all the edges of the Graph g
    def add_all_edges(self, g):
        print("Inserting edges...")
        
        total_nodes = self.rows * self.columns
        e = 1

        # adding edges horizontally
        for node in range(total_nodes-1):
            
            if e != self.columns:
                g.add_edge(fromNode=str(node), toNode=str(node+1), value=1)
                e = e + 1
            else:
                e = 1

        # e = 1
        total_nodes = self.columns * (self.rows - 1)
        # adding edges vertically
        for node in range(total_nodes):
            g.add_edge(fromNode=str(node), toNode=str(node+self.columns), value=1)

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
