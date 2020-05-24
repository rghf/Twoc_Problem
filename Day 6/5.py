import math
def isPefectSquare(x):
    y = int(math.sqrt(x))
    return y*y==x

def isFib(n):
    return(isPefectSquare(5*n*n+4) or isPefectSquare(5*n*n-4))


l = list(map(int, input().split()))
z = sum(l)
print("Yes" if isFib(z)==True else "No")
