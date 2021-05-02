
parent = {}

def makeSet(i):
    
    parent[i] = i
    
def Find(k):
    
    if parent[k] == k:
        return k
    return Find(parent[k])

def Union(a, b):
 
    x = Find(a)
    y = Find(b)
 
    parent[x] = y
 
 
def kruskalAlgo(edges, N):
 
    total_min_weight=0
    MST = []
 

    for i in range(N):
        makeSet(i)
 
    index = 0
 
    edges.sort(key=lambda x: x[2])
 
    while len(MST) != N - 1:
 
        (src, dest, weight) = edges[index]
        index = index + 1
 

        x = Find(src)
        y = Find(dest)
 

        if x != y:
            MST.append((src, dest, weight))
            Union(x, y)
            total_min_weight+=weight
 
    return MST,total_min_weight
 

edges = [
    (0, 1, 7), (1, 2, 8), (0, 3, 5),
    (1, 3, 9), (1, 4, 7), (2, 4, 5),
    (3, 4, 15), (3, 5, 6), (4, 5, 8),
    (4, 6, 9), (5, 6, 11)
]
 
N = 7
 
mst,min_w = kruskalAlgo(edges, N)
 
print('Edges in the constructed MST:',mst)
print('Minimum Cost Spanning Tree:',min_w)