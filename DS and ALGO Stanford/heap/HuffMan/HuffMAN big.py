def read_code(filepath):
    """ read the weights for each symbol from txt file
        return: a python dictionary (key: symbol id, value: (weight, min coding length, max coding length)
    """
    code = {}
#     s="abcdefghijklmno"
    with open(filepath) as f:
        lines = f.readlines()
        for i, line in enumerate(lines[1:]):
            code[str(i)] = int(line.split()[0])
#             code[s[i]] = int(line.split()[0])
    return code



code = read_code('huffman_small.txt')

vals=[]
for s in code:
    vals.append([s,code[s]])
    vals.sort(key=lambda x: x[1])
    
    
    
    
left=[]
right=[]
def tree(vals):
    
    
    
    for values in vals:#in range((len(vals)-1)):
    #     print((vals[1][0]))
    #     if ivalues+1==len(vals):
#         Nodes[str((vals[0][0]+vals[1][0]))]=[[vals[0][0]],[vals[1][0]]]
    #     break
        
        left.append(vals[0][0])
        l=vals.pop(0)
        
#         print(vals,"l:",l)
        right.append(vals[0][0])
        r=vals.pop(0)
#         print(vals,"r:",r)
        vals.append([l[0]+r[0],l[1]+r[1]])
        vals.sort(key=lambda x: x[1])#inplace---changes the main vals position
#         sorted(vals, key=lambda x: x[1])#not in place ----doesn't change
#         print("vals",vals)
        

        if len(vals)>1:
           tree(vals)
        
      
    return 

print(tree(vals))


pol=[]
for key in code.keys():
    pol.append(key)

# pol="abcdefghijkl"
for i in range(len(pol)):
    po=pol[i]
    M=""
    for i in range(len(left)):
        
        if po in left[i]:
#             print("l",i)
            
            M=M+"0"
        elif po in right[i]:
#             print(i)
            M=M+"1"
    print(po,M[::-1],len(M[::-1]))