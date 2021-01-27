#min_heap

# arr=[1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]#[4, 10, 3, 5, 1]#[4,1,3,2,16,9,10,14,8,7]#[5,7,9,1,3]
arr=[16, 14, 10, 1, 7, 9, 3, 2, 4, 8]
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
    #else:
    return arr 
    
# print(Min_heapify(arr))


# min_sort
s=[]
for i in range(len(Min_heapify(arr))):
    if Min_heapify(arr)!=[]:
#         Min_heapify(arr)[0]=Min_heapify(arr)[len(Min_heapify(arr))-1]
        s.append(Min_heapify(arr).pop(0))
print (s)
