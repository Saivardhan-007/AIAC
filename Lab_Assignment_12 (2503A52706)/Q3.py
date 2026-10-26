'''Question 3: Search for the First Element
Given the sorted array:
A = [8, 16, 24, 32, 40, 48, 56, 64, 72]
Apply Binary Search to find the key 8.
Find:
1. The low, high, and mid values in each iteration.
2. The elements checked.
3. The index of the key.
4. The number of comparisons required.
'''

A = [8, 16, 24, 32, 40, 48, 56, 64, 72]
key = 8

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
