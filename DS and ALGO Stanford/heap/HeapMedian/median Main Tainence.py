
def Min_heapify(p):
#     L=2*i+1
#     R=2*i+2
    swap=0
    for i in range(len(p)):
        #swap=0
        L=2*i+1
        R=2*i+2
        if (L and R)<=int(len(p)-1):
            if (p[i]>p[L] and p[R]>=p[L]):
                p[i],p[L]=p[L],p[i]
                swap+=1
            elif p[i]>p[R]:
                p[i],p[R]=p[R],p[i]
                swap+=1
        elif L==int(len(p)-1) and R>int(len(p)-1):
            if p[i]>p[L]:
                p[i],p[L]=p[L],p[i]
    if swap!=0:
        Min_heapify(p)
    #else:
    return p


def Max_heapify(p):
#     L=2*i+1
#     R=2*i+2
    swap=0
    for i in range(len(p)):
        #swap=0
        L=2*i+1
        R=2*i+2
        if (L and R)<=int(len(p)-1):
            if (p[i]<p[L] and p[R]<=p[L]):
                p[i],p[L]=p[L],p[i]
                swap+=1
            elif p[i]<p[R]:
                p[i],p[R]=p[R],p[i]
                swap+=1
        elif L==int(len(p)-1) and R>int(len(p)-1):
            if p[i]<p[L]:
                p[i],p[L]=p[L],p[i]
    if swap!=0:
        Max_heapify(p)
    #else:
    return p
# data=[10,9,11,8,12,7,13,6,14,5]
# data=[0,-1,1,-2,2,-3,3,-4,4,-5,5]
# data=[12,4,5]
# data=[3,4,5,7,8,12]
# data=[1,2,3,4,5,6,7,8,9,10]
# data=[12,4,5,3,8,7]
# data=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
# data=[5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
data=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
# data=[1,2,3,4]
Max=[]
Min=[]
# print( ( float((Max[0]+Min[0])/2))

#for value in data:
    

if Max==[]:
    Max.append(data.pop(0))
    print(Max[0])
    
    
elif Max!=[] and Min==[]:
    Min.append(data.pop(0))
    print(float((Max[0]+Min[0])/2))


for value in data:
    if value > Max[0]:#Max[0]:
        Min.append(value)
        Min_heapify(Min)# Heap_min(Min)
        
       
    else :
        Max.append(value)
        Max_heapify(Max)#Heap_max(Max)

    if len(Max)-len(Min)==0:
        print((float((Max[0]+Min[0])/2)))
        
    if len(Max)-len(Min)==1:
        Max_heapify(Max)
        Min_heapify(Min)
        print((Max[0]))
        
    if len(Min)-len(Max)==1:
        Min_heapify(Min)
        Max_heapify(Max)
        print((Min[0]))
        
    if len(Max)-len(Min)==2:
        Min.append(Max.pop(0))
        Min_heapify(Min)# Heap_min(Min)
        print((float((Max[0]+Min[0])/2)))
        # Heap_min(Max)

    if len(Min)-len(Max)==2:
        Max.append(Min.pop(0))
        # Heap_min(Min)
        Max_heapify(Max)# Heap_min(Max)
        print( float((Max[0]+Min[0])/2))
        
        
