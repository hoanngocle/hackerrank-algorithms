# 8. Solution: print mini Max sum in arry

def miniMaxSum(arr):
    arr = sorted(arr)
    min = sum(arr) - arr[len(arr) - 1]
    max = sum(arr) - arr[0]
    
    print(min, max)

array = [1,2,3,4,5]
miniMaxSum(array)