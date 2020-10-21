def pal_check(st):
    stack = []
    letters = list(st)  # 문자열을 리스트 화
    n = len(st)         # 문자열의 길이 n
    h = n//2            # 앞부분까지의 인덱싱을 위한 h
    
    # 앞부분을 stack에 push 한다.
    for i in range(h):
        stack.append(letters[i])
    
    # 짝수면
    if n%2 == 0:

        for i in range(h,n):
            temp = stack.pop()
            if temp != letters[i]:
                print('회문이 아닙니다')
                break
    
    
    # 홀수면
    else:

        for i in range(h+1,n): # 홀수는 중간 문자를 버리고 지나감
            temp = stack.pop()
            if temp != letters[i]:
                print('회문이 아닙니다')
                break
    
    
    
    
    # 비교하면서 stack에서 하나씩 뺴고, 스택이 비면 회문.
    
    if len(stack) == 0:
        print('회문입니다')

inp = input("회문을 확인할 문자를 입력하세요: ")
pal_check(inp)
