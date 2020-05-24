from itertools import permutations
l = (["".join(x) for x in permutations("218765")])
l.sort()
for i in range(len(l)):
    if l[i]=="218765":
        print(l[i+1])
