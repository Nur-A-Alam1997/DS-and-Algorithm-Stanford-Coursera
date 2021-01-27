# def load_graph():
#     """
#     load the graph from the txt file
#     :return: python dictionary representing the graph structure
#     """


graph = {}
with open('kargerMinCut4.txt') as f:
    for ln in f:
        line = ln.split()
#         print(line)
        if line:
            vertices = [x for x in line]
            graph[int(line[0])] = vertices
            l=(([list(graph.keys())]))
            print(l)
        

# 
# 
# 
#         


# 
# line=[[45, 3, 3, 3, 3, 3, 3, 3, 3, 3,89],[43]]
# 
# print(line[1])