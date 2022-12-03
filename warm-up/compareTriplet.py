# 3. Solution: Compare triplet

def compareTriplets(a, b):
    countA = 0
    countB = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            countA += 1
        elif a[i] < b[i]:
            countB += 1
    
    return [countA, countB]

# Input
array1 = [1, 2, 3, 4, 10, 11]
array2 = [11, 5, 2, 4, 9, 18]
output = compareTriplets(array1, array2)

# Print output
print("==================")
print("Output: " + str(output))