N = int(input("Enter the value of N: "))
a = 0
b = 1
print("Fibonacci series are:", N)
for i in range(N):
    print(a, end = " ")
    c = a + b
    a = b
    b = c
