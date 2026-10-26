'''Question 4: Search for an Element in a Larger Array
Given the sorted array:
A = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59]
Apply Binary Search to find the key 47.
Find:
1. The low, high, and mid values at each iteration.
2. The elements checked at each step.
3. The final index of the key.
4. The total number of comparisons.
'''

A = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59]
key = 47

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