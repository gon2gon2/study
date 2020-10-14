stack = []
lst1 = ['(', '{', '(', '(', ')', ')', '}', ')']
lst2 = ['(', '{',')', ')']
def opp(x):
    if x == '(':
        return ')'
    elif x == '{':
        return '}'
def pare(lst):
    print("짝을 확인합니다")
    for i in lst:
        
        if i == "{" or i == "(":
            stack.append(i)
            print('stack에'+i+'를 추가했습니다',stack)
            
            
        elif i == "}" or i == ")":
            a = stack.pop()
            if i != opp(a):
                print('회문이 아닙니다')
                break
            
    if len(stack) == 0:
        print('stack:',stack)
        print('짝이 맞습니다')

pare(lst1)
pare(lst2)