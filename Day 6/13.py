from itertools import combinations
arr = list(map(float,input().split()))
comb = combinations(array,3)
l = []
for a,b,c in comb:
    if 1<(a+b+c)<2:
        l.append((a,b,c))
print(l)
