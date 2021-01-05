# 16으로 나누고 그때마다의 나머지를 스택에 쌓아서 대응하는 것 출력하면 될듯
dic = {10: "A", 11:"B",12:"C",13:"D",14:"E",15:"F"}
n = int(input("숫자 입력: "))
stack = []

while n>16:
    r = n%16
    if r >=10:
        stack.append(dic[r])
    else:
        stack.append(str(r))
    n -= r*16
if n>0:
    stack.append(str(n))
else:
    stack.append("0")
# print(stack[::-1])
p = ""
for i in stack:
    p += i
print(p)