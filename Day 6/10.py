k = int(input("Enter the numbers of list:"))
CompList = []
for i in range(k):
    TempList = list(map(int,input().split()))
    TempList.sort()
    CompList.extend(TempList)

print(sorted(CompList))
