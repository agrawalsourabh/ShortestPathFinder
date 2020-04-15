from _collections import defaultdict
import sys
# from CreateGraph import createGraph


def get_heuristic(start_node, end_node):
    D = 1
    return D * abs(int(start_node) - int(end_node))


def astar(graph, start_node, end_node):
    G = {}
    F = {}
    path = {}

    closed_vertex = []
    open_vertex = set()

    G[start_node] = 0
    F[start_node] = get_heuristic(start_node, end_node)

    open_vertex.add(start_node)

    previous_node = start_node

    while len(open_vertex) > 0:
        current = None

        # maximum value
        current_f_score = sys.maxsize * 2 + 1

        # code required to select the current node
        print("running for")
        for node in open_vertex:
            print("node: " + node)
            print("F: " + str(F[node]))
            print(current_f_score)

            if current_f_score > F[node]:
                current_f_score = F[node]
                current = node

        open_vertex.remove(current)
        closed_vertex.append(current)

        # path[current] = previous_node

        if current == end_node:
            shortest_path = shortest_path_s_d(initial=start_node, endNode=end_node, path_edge=path)
            return shortest_path[::-1], closed_vertex

        for neighbour in graph.getEdges(fromNode=current):
            print("inside for loop")
            print("neighbour: " + neighbour)

            if neighbour not in closed_vertex:
                print("neighbour " + neighbour)

                open_vertex.add(neighbour)

                if neighbour not in G.keys():
                    print("inside G")
                    G[neighbour] = G[current] + 1
                    path[neighbour] = current
                else:
                    if G[neighbour] > G[current] + 1:
                        G[neighbour] = G[current] + 1
                        path[neighbour] = current

                if neighbour not in F.keys():
                    print("inside f")
                    F[neighbour] = G[neighbour] + get_heuristic(neighbour, end_node)
                    print("Node: " + neighbour)
                    print("F: " + str(F[neighbour]))
                else:
                    f_score = G[neighbour] + get_heuristic(neighbour, end_node)
                    if F[neighbour] > f_score:
                        F[neighbour] = G[neighbour] + get_heuristic(neighbour, end_node)



def shortest_path_s_d(initial, endNode, path_edge):
    shortest_path = []
    previous_node = endNode
    while 1:
        shortest_path.append(path_edge[previous_node])
        previous_node = path_edge[previous_node]

        if previous_node == initial:
            break

    return shortest_path


# if __name__ == "__main__":
#     g = createGraph(rows=3, cols=3)
#     print(astar('6', '2', g))
