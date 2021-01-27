#max_heap sort for 2D list on 2nd or tertiary position
arr=[[11, 12, 5, 2], [15, 6,10,8], [10, 8, 12, 5], [12,15,8,6]]
# arr=[1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]#[4, 10, 3, 5, 1]#[4,1,3,2,16,9,10,14,8,7]#[5,7,9,1,3]
# arr=[16, 14, 10, 1, 7, 9, 3, 2, 4, 8]
position=0
def Max_heapify(p):
#     L=2*i+1
#     R=2*i+2
    swap=0
    for i in range(len(arr)):
        #swap=0
        L=2*i+1
        R=2*i+2
        if (L and R)<=int(len(arr)-1):
            if (arr[i][position]<arr[L][position] and arr[R][position]<=arr[L][position]):
                arr[i],arr[L]=arr[L],arr[i]
                swap+=1
            elif arr[i][position]<arr[R][position]:
                arr[i],arr[R]=arr[R],arr[i]
                swap+=1
        elif L==int(len(arr)-1) and R>int(len(arr)-1):
            if arr[i][position]<arr[L][position]:
                arr[i],arr[L]=arr[L],arr[i]
    if swap!=0:
        Max_heapify(p)
    #else:
    return arr 
    
#print(Max_heapify(arr))
#max sort
s=[]
for i in range(len(Max_heapify(arr))):
    if Max_heapify(arr)!=[]:
#         Min_heapify(arr)[0]=Min_heapify(arr)[len(Min_heapify(arr))-1]
        s.append(Max_heapify(arr).pop(0))
print (s)
