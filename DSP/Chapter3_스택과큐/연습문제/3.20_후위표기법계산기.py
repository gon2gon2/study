stack = []
four = ['+','-','*','/']       # 사칙연산 기호 집합

def postcal(st):
    n = len(st)
    temp = list(st) 

    # 연산 기호인지 확인
    for i in temp:
        
        if i in four:

            rear = int(stack.pop())
            front = int(stack.pop())

            # 각 연산 기호에 해당하는 연산을 수행해서 스택에 저장한다.
            if i == '+':
                pare = front + rear        
                stack.append(pare)               
            elif i == '-':
                pare = front - rear
                stack.append(pare)
            elif i == '*':
                pare = front * rear
                stack.append(pare)
            elif i == '/':
                pare = front / rear
                stack.append(pare)
        else:    
            pare = i
            stack.append(pare)


    return stack[-1]


x = input('후위표기법으로 된 식을 입력하세요')
postcal(x)