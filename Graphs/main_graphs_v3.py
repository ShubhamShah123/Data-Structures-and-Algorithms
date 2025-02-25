from Graphs import UndirectedGraph, DirectedWeigtedGraph, DisjointSet, DirectedGraph
from OtherGraphsFunctions import getMatrixFromEdges

n, m = 6, 8
u_graph = UndirectedGraph(n, m)
edgesList = [
    (0,1,4),
    (0,2,4),
    (1,2,2),
    (2,3,3),
    (2,5,6),
    (2,4,1),
    (3,5,2),
    (4,5,3)
]

for u, v, w in edgesList:
    u_graph.AddEdges(u, v, w)


source = 0
output_dist = u_graph.DijkstraAlgorithmMethod1(u_graph.num_nodes, u_graph.adj_list, source)
print(f"\n27(i). Minimum distance from src={source} to all other nodes using Dijkstra's Algorithm (Method1 - Priority Queue): {output_dist}")
output_dist = u_graph.DijkstraAlgorithmMethod2(u_graph.num_nodes, u_graph.adj_list, source)
print(f"\n27(ii). Minimum distance from src={source} to all other nodes using Dijkstra's Algorithm using (Method2 - Set) output: {output_dist}")

n, m = 5, 6
u_graph = UndirectedGraph(n, m)
edgesList = [
    (1,2,2),
    (1,4,1),
    (2,1,2),
    (2,3,4),
    (3,4,3),
    (3,5,1),
    (4,1,1),
    (4,3,3),
    (5,2,5),
    (5,3,1)
]

source = 1
destination = 5

for u, v, w in edgesList:
    u_graph.AddEdges(u, v, w)

path = u_graph.GetShortestPathDijkstra(source, destination)
print(f"\n28. Shortest Path using Dijkstra: {path}")

print("\n35. Floyed Warshall Algorithm.")
n, m = 4, 6
dag = DirectedWeigtedGraph(n, m)
edgesList = [
    [0,1,2],
    [1,0,1],
    [3,0,3],
    [3,2,4],
    [3,1,5],
    [1,2,3]
]
for u, v, w in edgesList:
    dag.AddEdges(u, v, w)

outputMatrix = dag.FloyedWardshall(dag.adj_matrix)
[print(row) for row in outputMatrix]

print(f"\n37. Minimum Spanning Tree using Prims Algorithm.")

n, m = 5, 6
u_graph = UndirectedGraph(n, m)
edgesList = [
    [0,1,2],
    [0,2,1],
    [1,2,1],
    [2,4,2],
    [2,3,2],
    [3,4,1]
]
for u,v,w in edgesList:
    u_graph.AddEdges(u, v, w)

mst_edge, mst_weight = u_graph.GetMSTPrims(n, u_graph.adj_list)
print(f">> Edges of MST: {mst_edge} | Total Cost: {mst_weight}")

print("\n38. Disjoint Sets: Union bv Rank")
ds_rank = DisjointSet(7)
edgesList = [
    [1,2],
    [2,3],
    [4,5],
    [6,7],
    [5,6],
    [3,4]
]

ds_rank.unionByRank(1,2)
ds_rank.unionByRank(2,3)
ds_rank.unionByRank(4,5)
ds_rank.unionByRank(6,7)
ds_rank.unionByRank(5,6)

if ds_rank.findUPar(3) == ds_rank.findUPar(4):
    print(">> YES")
else:
    print(">> NO")

ds_rank.unionByRank(3,4)

if ds_rank.findUPar(3) == ds_rank.findUPar(4):
    print(">> YES")
else:
    print(">> NO")


print("\n39. Disjoint Sets: Union bv Size")

ds_size = DisjointSet(7)

ds_size.unionBySize(1,2)
ds_size.unionBySize(2,3)
ds_size.unionBySize(4,5)
ds_size.unionBySize(6,7)
ds_size.unionBySize(5,6)

if ds_size.findUPar(3) == ds_size.findUPar(4):
    print(">> YES")
else:
    print(">> NO")

ds_size.unionBySize(3,4)

if ds_size.findUPar(3) == ds_size.findUPar(4):
    print(">> YES")
else:
    print(">> NO")

print("\n40. Kruskal's Algorithm:")

def kruskalAlgorithm(V: int, adjList: list):
    edges = []
    for i in range(1, len(adjList)):
        for it in adjList[i]:
            adjNode = it[0]
            adjWt = it[1]
            node = i
            edges.append([adjWt, node, adjNode])
    sortedEdges = sorted(edges)
    ds = DisjointSet(V)
    mstWt = 0
    for wt,u,v in sortedEdges:
        if (ds.findUPar(u) != ds.findUPar(v)):
            mstWt += wt
            ds.unionBySize(u, v)

    return mstWt

V, E = 6, 9
u_graph = UndirectedGraph(V, E)
edgesList = [
    [5,4,9],
    [5,1,4],
    [4,1,1],
    [4,3,5],
    [4,2,3],
    [1,2,2],
    [3,2,3],
    [3,6,8],
    [2,6,7]
]

for u,v,w in edgesList:
    u_graph.AddEdges(u, v, w)

output = kruskalAlgorithm(V, u_graph.adj_list)
print(f">> Output of Kruskal's Algorithm: {output}")

print("\n47. Strongly Connected Components (SCC) or Kosaraju's Algorithm.")
V, E = 8, 10
edgesList = [
    [0,1],
    [1,2],
    [2,0],
    [2,3],
    [3,4],
    [4,5],
    [5,6],
    [6,7],
    [6,4],
    [4,7]
]
d_graph = DirectedGraph(V,E)
for u, v in edgesList:
    d_graph.AddEdges(u, v)

output = d_graph.KosarajuAlgorithm(V, d_graph.adj_list)
print(f">> Output: {output}")

print("\n49. Articulation Points")
V, E = 7, 8
u_graph = UndirectedGraph(V, E)
edgesList = [
    [0,1],
    [0,2],
    [0,3],
    [2,4],
    [2,5],
    [4,6],
    [6,5],
    [2,3]
]
for u, v in edgesList:
    u_graph.AddEdges(u, v)

output = u_graph.ArticulationPoints(V, u_graph.adj_list)
print(f">> List of points: {output}")