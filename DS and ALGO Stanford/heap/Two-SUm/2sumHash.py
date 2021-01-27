from time import time

#slick O(n) implementation for the 2sum problem, using hash tables!
def twoSum(arr):
	#for blazing fast look ups
	hashTable = set(arr)
        
	
	count = 0
	for t in range(-10000, 10000 + 1):
		for x in hashTable:
			if t - x in hashTable and t - x != x:
				print((x, t - x), count)
				count += 1

				#if a valid x, y pair is found, don't bother looking further 
				break

	return count

#init
if __name__ == '__main__':
	startTime = time()
	print(twoSum(list(map(int, open('2sum_test.txt').read().splitlines())))) #ans = 427
# 	print(twoSum([1, 2, 3]))
	print(time() - startTime)