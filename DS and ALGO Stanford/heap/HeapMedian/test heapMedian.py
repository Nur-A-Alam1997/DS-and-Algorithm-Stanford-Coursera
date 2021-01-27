import heapq

maxh = []
minh = []
# vals=[5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
# vals=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
# vals=[1,2,3,4]
vals=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
# vals=[12,4,5,3,8,7]
# vals=[0,-1,1,-2,2,-3,3,-4,4,-5,5]
# vals=[10,9,11,8,12,7,13,6,14,5]
for val in vals:

    # Initialize the data-structure and insert/push the 1st streaming value
    if not maxh and not minh:
        heapq.heappush(maxh,-val)
        print (float(val))
    elif maxh:

        # Insert/push the other streaming values
        if val>maxh[0]:
            heapq.heappush(minh,val)
        else :
            heapq.heappush(maxh,-val)

        # Calculate the median
        if len(maxh)==len(minh):
            print (float(-maxh[0]+minh[0])/2)
        elif len(maxh)==len(minh)+1:
            print (float(-maxh[0]))
        elif len(minh)==len(maxh)+1:
            print (float(minh[0]))

        # If min-heap and max-heap grow unbalanced we rebalance them by
        # removing/popping one element from a heap and inserting/pushing
        # it into the other heap, then we calculate the median
        elif len(minh)==len(maxh)+2:
            heapq.heappush(maxh,-heapq.heappop(minh))
            print (float(-maxh[0]+minh[0])/2)
        elif len(maxh)==len(minh)+2:
            heapq.heappush(minh,-heapq.heappop(maxh))
            print (float(-maxh[0]+minh[0])/2)