a,b = map(int,input().split(' '))
c = input()
p = a*b
for i in c.split():
    print(int(i) - p,end=' ')
