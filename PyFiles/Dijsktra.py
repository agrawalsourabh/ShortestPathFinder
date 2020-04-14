from queue import LifoQueue


def shortest_path_s_d(initial, endNode, path_edge):
    shortest_path = []
    previous_node = endNode
    while 1:
        shortest_path.append(path_edge[previous_node])
        previous_node = path_edge[previous_node]

        if previous_node == initial:
            break

    return shortest_path


def dijsktra(graph, initial, endNode):
    visited = {initial: 0}
    path = set()
    path_edge = {}
    traverse = []
    traverse.append(initial)

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.getEdges(min_node):
            weight = current_weight + graph.getDistance(min_node, edge)
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                traverse.append(edge)
                path_edge[edge] = min_node
                path.add(min_node)

        if endNode in visited:
            break

    shortest_path = shortest_path_s_d(initial, endNode, path_edge)

    return shortest_path[::-1], visited, traverse

# # creating graph
# # and initializing nodes and edges


# g = Graph.Graph()

# # adding nodes
# for i in range(3):
#     for j in  range(3):
#         g.add_node(str(i)+str(j))

# # adding edges
# g.add_edge('00', '01', 1)
# g.add_edge('00', '10', 1)
# g.add_edge('01', '02', 1)
# g.add_edge('01', '11', 1)
# g.add_edge('02', '12', 1)
# g.add_edge('10', '11', 1)
# g.add_edge('10', '20', 1)
# g.add_edge('11', '12', 1)
# g.add_edge('11', '21', 1)
# g.add_edge('12', '22', 1)
# g.add_edge('20', '21', 1)
# g.add_edge('21', '22', 1)


# g.displayNodes()

# # print("Edges")
# # g.displayEdges()

# # print("Distances")
# # g.displayDistances()

# visited, path, path_edge = dijsktra(g, '00', '21')
# # print(visited)
# print(path)


# # print(g.getDistance('00', '01'))
# # print(g.getEdges('00'))
