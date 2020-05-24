l  = list(map(int, input().split()))
x = []
for i in l:
    if i==0 or i==1:
        x.append(i)
    else:
        print("Enter 0 or 1 only")
        break

print(sorted(x))
