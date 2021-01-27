import heapq


def dijkstra(graph, start, end):
    heap = [(0, start)]  # cost from start node,end node
    visited = []
    while heap:
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue
        visited.append(u)
        if u == end:
            return cost
        for v, c in G[u]:
            if v in visited:
                continue
            next = cost + c
            heapq.heappush(heap, (next, v))
    return (-1, -1)


G = {'A': [['B', 2], ['C', 5]],
     'B': [['A', 2], ['D', 3], ['E', 1]],
     'C': [['A', 5], ['F', 3]],
     'D': [['B', 3]],
     'E': [['B', 1], ['F', 3]],
     'F': [['C', 3], ['E', 3]]}

shortDistance = dijkstra(G, 'D', 'C')
print(shortDistance)