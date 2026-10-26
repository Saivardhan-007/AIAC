'''Question 5: Binary Search with Duplicate Values
Given the sorted array:
A = [10, 20, 20, 20, 30, 40, 50, 60, 70]
Apply a modified Binary Search to find the first occurrence of key 20.
Find:
1. The low, high, and mid values at each iteration.
2. How the search continues after finding the key.
3. The index of the first occurrence of 20.
4. The total number of iterations.
'''

A = [10, 20, 20, 20, 30, 40, 50, 60, 70]
key = 20

low = 0
high = len(A) - 1
result = -1
count = 0

while low <= high:
    mid = (low + high) // 2
    count += 1

    print("Low =", low, "High =", high, "Mid =", mid)
    print("Middle element =", A[mid])

    if A[mid] == key:
        result = mid
        high = mid - 1
    elif A[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if result != -1:
    print("First occurrence of", key, "is at index:", result)
else:
    print("Key not found")

print("Total iterations:", count)