class Node:                         # 노드 클래스
    def __init__(self,item,n)       # 노드 생성자
        self.item = item            # 
        self.next = n





def add(item):                      # add 함수
    global size
    global front
    global rear


    new_node = Node(item, None)     # 새로운 노드를 만들어 new node

    if size == 0:                   # 빈 리스트면         size == 0
        front = new_node            # 맨 앞에 삽입        front
    
    else:                           # 이미 항목이 있으면  size != 0
        rear.next = new_node        # 맨 뒤에 삽입        rear.next

    rear = new_node                 # 빈 리스트든 항목이 있던 맨 뒤로 서야 되니까 rear로 저장
    size += 1                       # 개수 +1







def remove():                       # remove 함수
    global size                     # 전역변수 size
    global front                    # 전역변수 front
    global rear                     # 전역변수 rear


    if size != 0:                   # 최소한 하나라도 있어야 실행됨
        fitem = front.item          # front의 아이템을 빼서 fitem에 저장
        front = front.next          # 두번째(front.next)를 front로 설정
        size -= 1                   # size에 -1 반영
        
        if size == 0:               # 빈 리스트면 
            rear = None             # ????rear = None????
        
        return fitem                # 원래 first였던 녀석을 출력








def print_q():                               # que를 출력하는 print_q 함수
    p = front                                # 첫번째를 p에 저장하고 시작
    print('front: ', end='')                 

    while p:                                 # 대기열의 맨 앞 p에 원소가 있는 동안


        if p.next != None:                   # 마지막 노드가 아니라면 (item.next가 None이 아니라면)
            print(p.item,'->    ',end='')    # item, ->를 출력한다


        else:                                # 참조(다음 항목)이 없으면
            print(p.item, end= '')           # 화살표 없이 아이템만 출력한다.


        p = p.next                           # 다음으로 넘어간다.
    print(' : rear')










front = None
rear =None
size =0
q = []
add('apple')
add('orange')
add('cherry')
add('pear')
print('사과,오렌지,체리,배 삽입 후: \t', end='')
print_q()
remove()
print('remove한 후:\t\t', end='')
print_q()
remove()
print('remove한 후:\t\t',end='')
print_q()
add('grape')
print('포도 삽입 후:\t\t', end='')
print_q()