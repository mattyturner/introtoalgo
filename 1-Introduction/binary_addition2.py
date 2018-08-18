#!/bin/python3
# 1.1-4
# For 2 n-length arrays of 1s and 0s representing a binary number.
# output an n+1 length array representing their summation 

def binaryAddition(a1, a2):	
	res = [0] * (len(a1) + 1);

	for j in range(len(a1)-1, -1, -1):
		summation = a1[j] + a2[j] + res[j + 1]
		res[j + 1] = summation % 2
		res[j] = summation // 2
	print(''.join(map(str, res)))
		


if __name__ == '__main__':
    arr1 = list(map(int, list(input())))	
    arr2 = list(map(int, list(input())))

    binaryAddition(arr1, arr2)

