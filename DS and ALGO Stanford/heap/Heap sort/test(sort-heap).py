#min_heap_sort

arr=[1,1,3,4,24,4,5,6,345,6,7,5,37353,3,35,4,5,24,2,7,7,5433,4,5,33,434342,2,1,213,132,121,112132,2,32]
def Min_heapify(p):
#     L=2*i+1
#     R=2*i+2
    swap=0
    for i in range(len(arr)):
        #swap=0
        L=2*i+1
        R=2*i+2
        if (L and R)<=int(len(arr)-1):
            if (arr[i]>arr[L] and arr[R]>=arr[L]):
                arr[i],arr[L]=arr[L],arr[i]
                swap+=1
            elif arr[i]>arr[R]:
                arr[i],arr[R]=arr[R],arr[i]
                swap+=1
        elif L==int(len(arr)-1) and R>int(len(arr)-1):
            if arr[i]>arr[L]:
                arr[i],arr[L]=arr[L],arr[i]
    if swap!=0:
        Min_heapify(p)
   
    return arr
    
# print((len(Min_heapify(arr))-1))
s=[]
for i in range(len(Min_heapify(arr))):
    if Min_heapify(arr)!=[]:
#         Min_heapify(arr)[0]=Min_heapify(arr)[len(Min_heapify(arr))-1]
        s.append(Min_heapify(arr).pop(0))
print ((s))

