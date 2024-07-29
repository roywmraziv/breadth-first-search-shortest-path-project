# List of edges (directed graph)
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
num_vertices = 4

def create_adjacency_matrix(num_of_vertices, edges):
    matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    print(matrix)

    for edge in edges:
        src, dst = edge
        matrix[src][dst] = 1
    
    return matrix


create_adjacency_matrix(num_vertices, edges)