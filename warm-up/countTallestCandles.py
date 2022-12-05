# 9. Solution: count tallest candles

def countTallestCandles(candles):
    le = max(candles)
    print(le)
    return candles.count(le)

def countTallestBasic(candles):
    max = 0
    countMax = 0
    for i in candles:
        if (i > max):
            max = i
            countMax = 1
        elif (i == max):
            countMax += 1

    return countMax

# Input
array = [23,45,43,23,67,67,4,67,2,7]
output = countTallestCandles(array)
output2 = countTallestBasic(array)

# Print output
print("==================")
print("Output: " + str(output))
print("Output2: " + str(output2))