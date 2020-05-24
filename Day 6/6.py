def isRotated(ar):
    x = min(ar)
    y = ar.index(x)
    beforeMin = ar[:y]
    afterMin = ar[y:]
    if (isSorted(beforeMin) and isSorted(afterMin)) and (ar[-1]<ar[y-1]):
        print("Yes")
    else:
        print("No")

def isSorted(ar):
    n = len(ar)
    if n==1 or n==0:
        return True
    return(ar[0]<=ar[1] and isSorted(ar[1:]))


array = [3,4,5,1,2]
isRotated(array)
