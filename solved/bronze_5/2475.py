n = input()
x = map(int,n.split())
N = 0
for i in x:
    N += i**2
print(N%10)