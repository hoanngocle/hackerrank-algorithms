# 2. Solution: Sum array

def simpleArraySum(array):
    sum = 0
    for x in array:
        sum += x
        
    return sum;

# Input
array = [1, 2, 3, 4, 10, 11]
arrayCount = len(array)
output = simpleArraySum(array)

# Print output
print("==================")
print("Output: " + str(output))

