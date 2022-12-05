# 7. Solution: print star case

def stairCase(n):
    for i in range(1, n+1):
        print(" " * (n - i) + "#" * i)

n = 6
stairCase(n)
