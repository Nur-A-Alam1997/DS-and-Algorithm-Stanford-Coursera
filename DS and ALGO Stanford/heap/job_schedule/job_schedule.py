from timeit import default_timer as timer

start = timer()





jobsFile = open('jobs_Test.txt','r')
lines = jobsFile.readlines()[1:]

jobs = []
length,weight = 0,0

for line in lines:
    weight = int(line.split()[0])
    length = int(line.split()[1])
    jobs.append([weight,length,weight - length])


# print(jobs)


position=2
def Max_heapify(p):
    swap=0
    for i in range(len(jobs)):
        L=2*i+1
        R=2*i+2
        if (L and R)<=int(len(jobs)-1):
            if (jobs[i][position]<jobs[L][position] and jobs[R][position]<=jobs[L][position]):
                jobs[i],jobs[L]=jobs[L],jobs[i]
                swap+=1
            elif jobs[i][position]<jobs[R][position]:
                jobs[i],jobs[R]=jobs[R],jobs[i]
                swap+=1
        elif L==int(len(jobs)-1) and R>int(len(jobs)-1):
            if jobs[i][position]<jobs[L][position]:
                jobs[i],jobs[L]=jobs[L],jobs[i]
    if swap!=0:
        Max_heapify(p)
    return jobs 
    
# print(Max_heapify(jobs))

#max sort---based on difference 
s=[]
for i in range(len(Max_heapify(jobs))):
    if Max_heapify(jobs)!=[]:
        s.append(Max_heapify(jobs).pop(0))
        
# print(s)

#max sort----based on weight

def Max_sort(p):
    
    
    def Max_heapify(p):
        
        swap=0
        for i in range(len(p)):
            L=2*i+1
            R=2*i+2
            if (L and R)<=int(len(p)-1):
                if (p[i][0]<p[L][0] and p[R][0]<=p[L][0]):
                    p[i],p[L]=p[L],p[i]
                    swap+=1
                elif p[i][0]<p[R][0]:
                    p[i],p[R]=p[R],p[i]
                    swap+=1
            elif L==int(len(p)-1) and R>int(len(p)-1):
                if p[i][0]<p[L][0]:
                    p[i],p[L]=p[L],p[i]
        if swap!=0:
            Max_heapify(p)
        return p    
    
# print(Max_heapify(p))
#max sort
    
    sort=[]
    for i in range(len(Max_heapify(path))):
      if Max_heapify(path)!= []:
          sort.append(Max_heapify(path).pop(0))
          
    return sort

#preprocess for secondary sorting based on first element
 
path=[]
newA=[]
for i in range(0,int((len(s)))):
  
  
  val1=s[i][2]
  if s[i][2]==val1 and i+1<len(s):
    path.append(s[i])
  
#     print(s[i][0],val1)
    val2=s[i+1][2]
  if i+1==len(s):
    path.append(s[i])
    newA.extend(Max_sort(path))
    
  if val1!=val2 :

    newA.extend(Max_sort(path))
    path=[]
    continue
    
print(len(newA))

        

#8:29
#completion time count
sumTime = 0
sumLength = 0 
for line in newA:
    sumLength += line[1]
    sumTime += line[0] * sumLength
print(sumTime)#69119377652

end = timer()
print( "Time in seconds",end - start) # Time in seconds