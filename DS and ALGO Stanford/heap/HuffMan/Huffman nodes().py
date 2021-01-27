#https://stackoverflow.com/questions/36965507/writing-a-dictionary-to-a-text-file
#https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list
#from collections import defaultdict

# data="aaaaaaaaaaaaaacddddddddddddddcccccccccccccccccccccccccccccddddddddaggggggggggggggggaaaaaffddddddddddddd"

data = "The frog at the bottom of the well drifts off into the great ocean"
frequency =dict()#defaultdict(int)
for symbol in data:
    if symbol in frequency.keys():
        frequency[symbol] +=1
    else:
        frequency[symbol] =1
    
print(frequency)
# f=open("Nodes.pdf","w")
vals=[]
for s in frequency:
    vals.append([s,frequency[s]])
    vals.sort(key=lambda x: x[1])
    
# print(vola)    
    
# Nodes={}
# vals=([["f",5],["b",9],["c",12],["d",13],["e",16],["a",45]])#,["q",76],["r",45]])
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


pol=""
for key in frequency.keys():
    pol+=key

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
    print(po,M[::-1])
        
# print(M[::-1])    


# for v in Nodes:
#     print(v,"-0-",Nodes[v][0][0],"-1-",Nodes[v][1][0])
       
# f.write(str(Nodes))
       
# f.close()
lol={'ab': [['a'], ['b']], 'cd': [['c'], ['d']], 'abcd': [['ab'], ['cd']]}
       
