G = {'A': [['B', 2], ['C', 5]],
     'B': [['A', 2], ['D', 3], ['E', 1]],
     'C': [['A', 5], ['F', 3]],
     'D': [['B', 3]],
     'E': [['B', 1], ['F', 3]],
     'F': [['C', 3], ['E', 3]]}


ul={heads:100000 for heads in G}
s='D'
ul[s]=0

visited=[]
def dijk(G,s,ul,t):
    mini=[]
    
    if s not in visited:
        visited.append(s)
        print(visited,"visited")
    for i in range(len(G[s])):
        child=G[s][i][0]
        
        #print(child)
        if child not in visited and ul[s]+G[s][i][1]<ul[child]:
            ul[child]=ul[s]+G[s][i][1]
            
            if mini==[]:
                mini.append(child)
                #print(mini)
            elif ul[mini[0]]>ul[child]:
                #print(ul[mini[0]],ul[child],"elif")
                mini.pop(0)
                mini.append(child)
    if mini!=[]:         
        dijk(G,mini[0],ul,t)
    return "shortest_distance:"+str(ul[visited.pop(0)])+"  absolute distance from source",ul[t],ul

print(dijk(G,s,ul,"F"))
