#!/bin/python3
# https://www.hackerrank.com/challenges/insertionsort2/problem

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
        print(' '.join(map(str, arr)))

# 1.1-2 sort in nonincreasing instead of nondecreasing order
def insertionSortDesc2(n, arr):
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
        print(' '.join(map(str, arr)))

# 1.1-3 search problem.
def search(v, arr):
    for j in range(0, len(arr)):
        if arr[j] == v:
            print(j)
            return
    print('nil')



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    search(n, arr)

