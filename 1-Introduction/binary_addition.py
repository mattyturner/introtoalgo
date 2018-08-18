#!/bin/python3
# 1.1-4
# For 2 n-length arrays of 1s and 0s representing a binary number.
# output an n+1 length array representing their summation 

flipper = tuple([1,0])
def binaryAddition(arr1, arr2):	
	#start with a 0 to pad our results
	res = [0]
	for j in range(0, len(arr1)):
		summation = arr1[j] + arr2[j]
		if summation != 2:
			res.append(summation)
		else:
			# if summation is 2 (i.e. both values were 1)
			# then working backwards flip preceding values until first 0 is encountered
			res = flipPreceding(res, j)
			for z in range(j, 0):
			res.append(0)		

	print(''.join(map(str, res)))

def flipPreceding(res, index):
	if index == -1:
		return res
	res[index] = flipper[res[index]]

	# a 1 was just flipped so we need to proceed until wil hit a 0 and flip it to 1
	if res[index] == 0:
		res = flipPreceding(res, index-1)
	return res


if __name__ == '__main__':
    arr1 = list(map(int, list(input())))	
    arr2 = list(map(int, list(input())))

    binaryAddition(arr1, arr2)

