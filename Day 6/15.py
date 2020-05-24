l = list(map(int,input().split()))

for i in range(0,len(l)):
    count = 0
    for j in range(0,i):
        if l[j]>=l[i]:
            count=1
            break

    for j in range(i + 1, len(l), 1):
        if (l[j] <= l[i]):
            count = 1
            break

    if count==0:
        print(l[i])
