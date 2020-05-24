l = list(map(int,input().split()))
k = int(input())
if k < len(l):
    l.sort()
    print("The kth sorted element in list is:",l[k-1])
