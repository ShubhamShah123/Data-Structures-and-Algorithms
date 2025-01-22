from Graphs_V1 import UndirectedGraph

def create_adj_matrix(numNodes, edges):
    matrix = [[0]*(numNodes+1) for _ in range(numNodes+1)]
    for edge in edges:
        u, v = edge
        matrix[u][v] = 1
        matrix[v][u] = 1  # Undirected graph
    
    return matrix

n, m = list(map(int, input("Enter n,m: ").split()))
u_graph = UndirectedGraph(n, m)
edgesList = []
for edges in range(m):
    node1, node2= list(map(int, input().split()))
    edgesList.append((node1, node2))
    u_graph.AddEdges(node1, node2)

print("+--+"*10)
startingNode = 1
bfsOutput = u_graph.BFSTraversal(startingNode)
print(f"1. Breadth First Traversal of The Graph: {bfsOutput}")

dfsOutput = u_graph.DFSTraversal(startingNode)
print(f"2. DFS travesal: {dfsOutput}")

adjMatrix = create_adj_matrix(n, edgesList)
counter = u_graph.NumberOfProvinces(adjMatrix, n)
print(f"3. Total Number of provinces: {counter}")

print(f"4. Detecting Cycle using BFS:")
# u_graph.display()
bfsOutput = u_graph.DetectCycleBFS(u_graph.num_nodes, u_graph.adj_list)
print(f">> Is Cycle Present? --> {bfsOutput} using BFS")
dfsOutput = u_graph.DetectCycleDFS(u_graph.num_nodes, u_graph.adj_list)
print(f">> Is Cycle Present? --> {dfsOutput} using DFS")