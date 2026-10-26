'''Question 7: Search for the Last Element
Given the array:
A = [11, 22, 33, 44, 55, 66, 77, 88]
Apply Linear Search to find the key 88.
Find:
1. The order in which elements are checked.
2. The index of the key.
3. The total number of comparisons.
4. The worst-case time complexity in terms of \(n\).
'''

A = [11, 22, 33, 44, 55, 66, 77, 88]
key = 88
count = 0

for i in range(len(A)):
    count += 1
    print("Checking element:", A[i])

    if A[i] == key:
        print("Key found at index:", i)
        print("Total comparisons:", count)
        break