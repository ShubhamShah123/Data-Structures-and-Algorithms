from Graphs_v2 import UndirectedGraph, DirectedGraph, DirectedWeigtedGraph
n, m = 4, 4

# n, m = list(map(int, input("Enter n,m: ").split()))
# u_graph = UndirectedGraph(n, m)
d_graph = DirectedGraph(n, m)
edgesList = [
	(1,0), (0,2), (1,3), (3,0)
]
for u, v in edgesList:
	d_graph.AddEdges(u, v)
# for edges in range(m):
#     node1, node2= list(map(int, input(f"edge {edges+1}: ").split()))
#     # u_graph.AddEdges(node1, node2)
#     d_graph.AddEdges(node1, node2)

# print(f"13. Check for BiPartite? --> {u_graph.isBipartite('bfs')} using BFS")
# print(f"14. Check for BiPartite? --> {u_graph.isBipartite('dfs')} using DFS")
# print(f"15. Cycle present in the directed graph? --> {d_graph.DetectCycle()}")
print(f"16. List of safe nodes : {d_graph.SafeNodes()}")
print(f"17. Topological Sort: {d_graph.TopologicalSort()}")
# print(f"18. Kahn's Algorithm output: {d_graph.KahnsAlgorithm()}")
# print(f"19. Cycle present ? using BFS: --> {d_graph.DetectCycleBFS()}")

# Course Schedule I and II
# n, p = list(map(int, input("Enter N, P: ").split()))
# p_list = []
# for i in range(p):
#     t1, t2 = list(map(int, input(f"task {i+1}: ").split()))
#     p_list.append((t1, t2))

# print("\n20. Course Schedule I and PreReqs")
# n, p = 5, 4
# d_graph = DirectedGraph(n, p)
# p_list = [
#     (1, 2),
#     (4, 3),
#     (2, 4),
#     (4, 1)
# ]

# output = d_graph.isPossibleCSI(n, p_list)
# print(f">> Can Tasks be performed? --> {output}")


# print("\n20. Course Schedule II and PreReqs")
# n, p = 2, 1
# d_graph = DirectedGraph(n, p)
# p_list = [
#     (1, 0)
# ]

# output = d_graph.isPossibleCSII(n, p_list)
# print(f">> Order of tasks? --> {output}")

print(f"21. Safe Nodes using BFS: {d_graph.SafeNodesBFS(d_graph.num_nodes, d_graph.adj_list)}")

# Alien Dict
print(f"22. Alien Dictionary.")
n, k = 5, 4
dict = [
	"baa",
	"abcd",
	"abca",
	"cab",
	"cad"
]
d_graph = DirectedGraph(k, k)
order = d_graph.AlienDict(k, dict)
print(f">> Order of the alien dictionary: {order}")

print("23. Shorted Path in DAG:")
n, m = 7, 8
wd_graph = DirectedWeigtedGraph(n, m)
edgeList = [
	(0,1,2),
	(1,3,1),
	(2,3,3),
	(4,0,3),
	(4,2,1),
	(5,4,1),
	(6,4,2),
	(6,5,3)
]
for n1, n2, w in edgeList:
	wd_graph.AddEdges(n1, n2, w)

source = 6
short_path_distance = wd_graph.GetShortestPath(source)
print(f">> SP from Source: {source} to each node: {short_path_distance}")

print("24. Shorted Path in UG:")
n, m = 9, 11
u_graph = UndirectedGraph(n, m)
edgeList = [
	(0,1,1),
	(0,3,1),
	(1,2,1),
	(1,3,1),
	(2,6,1),
	(3,4,1),
	(4,5,1),
	(5,6,1),
	(6,7,1),
	(7,8,1),
	(6,8,1)
]
for u, v, w in edgeList:
	u_graph.AddEdges(u, v, w)

source = 0
short_path_distance = u_graph.GetShortesPathUG(source)
print(f">> SP from Source: {source} to each node: {short_path_distance}")