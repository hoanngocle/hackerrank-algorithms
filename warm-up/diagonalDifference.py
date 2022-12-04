# 5. Solution: count diagonal Difference

def diagonalDifference(arr, n):
    sumFirst = 0
    sumSecond = 0
    j = n - 1;
    for i in range(n):        
        sumFirst += arr[i][i]
        sumSecond += arr[j][i]
        j -= 1

    return abs(sumFirst - sumSecond) 

# Input
n = 5
array = [[23,45,43,23,45], [45,67,54,32,45], [89,90,87,65,44], [23,45,67,32,10], [26,43,6,39,11]]
output = diagonalDifference(array, n)

# Print output
print("==================")
print("Output: " + str(output))