L = list(map(int, input().split()))
a = L[0]
b=L[1]

A=[]
for i in range(1,min(a, b)):
    if (a % i and b % i == 0):
        A.append(i)
l = len(A)
print(l)
