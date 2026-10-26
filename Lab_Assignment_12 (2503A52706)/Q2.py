'''Question 2: Search for an Unsuccessful Key
Given the sorted array:
A = [12, 18, 24, 30, 36, 42, 48, 54, 60, 66]
Apply Binary Search to search for the key 50.
Find:
1. The values of low, high, and mid at each iteration.
2. The elements compared with the key.
3. The final result when the key is not present.
4. The total number of comparisons.
'''

A = [12, 18, 24, 30, 36, 42, 48, 54, 60, 66]
key = 50

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
        break
    elif A[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Key not found")

print("Total comparisons:", count)
