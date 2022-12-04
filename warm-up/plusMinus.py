# 5. Solution: plus Minus

def plusMinus(arr, n):
    countZero = 0
    countPositive = 0
    countNegative = 0
    for i in arr:
        if i == 0:
            countZero += 1
        elif i > 0:
            countPositive += 1
        else:
            countNegative += 1
    print(round(countPositive / n, 6))
    print(round(countNegative / n, 6))
    print(round(countZero / n, 6))


# Input
n = 7
array = [23, 45, 43, 0, -11, -83, -7]
plusMinus(array, n)

# Print output
print("==================")