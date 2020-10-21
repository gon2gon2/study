from collections import deque
dq = deque('data')
for elem in dq:
    print(elem.upper(), end='')
print()
dq.append('r')             # default는 오른쪽에 삽입
dq.appendleft('k')         # appendleft를 통해 왼쪽에 삽입 가능
print(dq)
dq.pop()                   # pop도 dafault는 오른쪽
dq.popleft()               # 왼쪽에서 뺼 수 있음
print(dq[-1])
print('x' in dq)
dq.extend('structure')             # extend로 추가 가능
dq.extendleft(reversed('python'))  # 맨 앞에서 하나씩 떼서 왼쪽에 
print(dq)                          # 붙이기 떄문에 reversed를 걸어줌