from collections import deque  # deque is a double ended queue optimized for fast appends and pops from both sides

# List of edges (directed graph)
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
num_vertices = 4

# method to create an adjancency matrix
def create_adjacency_matrix(num_of_vertices, edges):
    matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    for edge in edges:
        src, dst = edge
        matrix[src][dst] = 1
    
    return matrix

# method to create a compliment adjacency matrix 
def create_comp_adjacency_matrix(matrix):
    num_nodes = len(matrix)

    # initializes the whole matrix to 1s 
    comp_matrix = [[1 for _ in range(num_nodes)] for _ in range(num_nodes)] 

    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                comp_matrix[i][j] = 0
            else:
                comp_matrix[i][j] = 1 - matrix[i][j]

    return comp_matrix

# breadth first search is a level-wise traversal so it explores nodes by level 
# breadth first search method
def bfs(start_node, graph):

    # create a set to hold the visited nodes (set is chosen because no repeat values)
    visited = set()

    # create a deque to hold the queue, initialized with the start node
    queue = deque([start_node])

    # nodes are processed in the order in which they are added (FIFO)
    while queue:
        node = queue.popleft()  # removes the leftmost element from the queue 

        if node not in visited:  # only process each node once 
            print(node, end=" ")

            visited.add(node)  # add the node into the visited set 

            # graph[node] returns the list of neighbors for the current node
            # the expression iterates through the neighbors returned and adds only if not previously visited 
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

