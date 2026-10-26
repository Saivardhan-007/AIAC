'''Question 6: Search for the First Element
Given the array:
A = [45, 20, 35, 10, 55, 60]
Apply Linear Search to find the key 45.
Find:
1. The elements checked.
2. The index of the key.
3. The number of comparisons required.
4. The best-case time complexity.
'''

A = [45, 20, 35, 10, 55, 60]
key = 45
count = 0

for i in range(len(A)):
    count += 1

    print("Checking element:", A[i])

    if A[i] == key:
        print("Key found at index:", i)
        print("Total comparisons:", count)
        break