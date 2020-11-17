n = int(input())
lst = []
c=[]
for i in range(n*2):
    lst.append(int(input()))
s1 = set(lst[:n])
s2 = set(lst[n:])
for i in s1:
    if i in s2:
        c.append(i)
cs=set(c)

if n in cs:
    cs.remove(n)


print('S1:',s1,'S2:',s2)
print('Result:',cs)