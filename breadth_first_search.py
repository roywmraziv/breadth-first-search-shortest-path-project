# List of edges (directed graph)
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
num_vertices = 4

def create_adjacency_matrix(num_of_vertices, edges):
    matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    for edge in edges:
        src, dst = edge
        matrix[src][dst] = 1
    
    return matrix


def create_comp_adjacency_matrix(matrix):
    num_nodes = len(matrix)

    comp_matrix = [[1 for _ in range(num_nodes)] for _ in range(num_nodes)]

    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                comp_matrix[i][j] = 0
            else:
                comp_matrix[i][j] = 1 - matrix[i][j]

    return comp_matrix