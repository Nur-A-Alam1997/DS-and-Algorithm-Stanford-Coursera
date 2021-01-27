p=[23,4,5,6,7,8]
def Max_sort(l):
    
    def Max_heapify(p):
        swap=0
        for i in range(len(p)):
            L=2*i+1
            R=2*i+2
            if (L and R)<=int(len(p)-1):
                if (p[i] <p[L]  and p[R] <=p[L] ):
                    p[i],p[L]=p[L],p[i]
                    swap+=1
                elif p[i] <p[R] :
                    p[i],p[R]=p[R],p[i]
                    swap+=1
            elif L==int(len(p)-1) and R>int(len(p)-1):
                if p[i] <p[L] :
                    p[i],p[L]=p[L],p[i]
        if swap!=0:
            Max_heapify(p)
        return p
    
# print(Max_heapify(p))
#max sort
    
    sort=[]
    for i in range(len(Max_heapify(p))):
      if Max_heapify(p)!= []:
          sort.append(Max_heapify(p).pop(0))
          
    return sort



print(Max_sort(p))

