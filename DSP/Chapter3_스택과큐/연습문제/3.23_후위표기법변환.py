def find_pare(lst):
    f_list = []
    s_list = []
    for i in range(len(lst)):
        
        if lst[i] == '(':
            f_list.append(i)
            
        elif lst[i] == ')':
            s_list.append(i)
            
    return f_list, s_list

def find_oper(lst):
    oper_idx = []
    four = ['+','-','*','/']
    for i in range(len(lst)):
        if lst[i] in four:
            oper_idx.append(i)
    return oper_idx

def rf(ab):
    stack =[]
    op_idx = find_oper(ab)[0]
    op = ab[op_idx]
    front = ab[1:op_idx]
    rear = ab[op_idx+1:-1]
    stack.append(front[0])
    stack.append(rear[0])
    stack.append(op)
    return stack

inp = input('중위표기법으로 표기된 식을 입력해주세요: ')
