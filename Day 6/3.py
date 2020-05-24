l = list(map(int,input().split()))
l.sort()
li = []
for i in l:
    if i>0:
        li.append(i)
print(li)
for i in range(len(li)):
    if li[i]!=(i+1):
        print("Smallest positive number missing from the list:",(i+1))
        break
