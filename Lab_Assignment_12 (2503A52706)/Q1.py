'''Question 1: Search for a Given Element
Given the sorted array:
A = [5, 10, 15, 20, 25, 30, 35, 40, 45]
Apply Binary Search to find the key 30.
Find:
1. The values of low, high, and mid at each iteration.
2. The middle element checked in each iteration.
3. The final position of the key (using 0-based indexing).
4. The total number of comparisons.
'''

A = [5, 10, 15, 20, 25, 30, 35, 40, 45]
key = 30

low = 0
high = len(A) - 1
count = 0

while low <= high:
    mid = (low + high) // 2
    count += 1

    print("Low =", low, "High =", high, "Mid =", mid)
    print("Middle element =", A[mid])

    if A[mid] == key:
        print("Key found at index:", mid)
        print("Total comparisons:", count)
        break
    elif A[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
