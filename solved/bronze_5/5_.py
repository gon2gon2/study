# 16으로 나누고 그때마다의 나머지를 스택에 쌓아서 대응하는 것 출력하면 될듯
n = int(input())
stack = []
while r>16:
    r = n%16
    n -= r
    stack.append(r)
    if r 
print(stack)
# print(n//15)  # //: 몫     %: 나머지# print(a+b, a-b, a*b, sep='\n')
