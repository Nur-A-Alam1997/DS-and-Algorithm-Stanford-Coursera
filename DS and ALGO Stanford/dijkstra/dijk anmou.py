  
# from collections import defaultdict

# def load_graph(filename):
#     """
#     load the graph structure from the txt file
#     :param filename: txt file path
#     :return: graph structure
#     """
graph ={} #defaultdict(list)
with open("dijk_Test.txt") as f:
    for lines in f:
        line = lines.split()
        if line:
            node = int(line[0])
            heads = [int(ln.split(',')[0]) for ln in line[1:]]
            costs = [int(ln.split(',')[1]) for ln in line[1:]]
            graph[node] = [[head, cost] for head, cost in zip(heads, costs)]

cv=10000
v={heads:100000 for heads in graph}

v[6]=0

for i in range(len(graph[6][0])):
    if graph[6][1][1]<cv:
        cv=graph[1][0][1]
#

print((graph))

print(v)
# print(load_graph("dijkstraTest.txt"))