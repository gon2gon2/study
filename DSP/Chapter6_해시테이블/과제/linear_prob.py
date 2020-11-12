# linear prob
class Linear_Probing:
    def __init__(self,size):
        self.M = size               # 테이블 크기 M
        self.a = [None]*size        # 해시테이블 a
        self.d = [None]*size        # 데이터 저장용 d
        self.N = 0                  # 항목 수 N

    def hash(self, key):            # 해시 함수
        return key % self.M         # key를 M으로 나눈 나머지 반환

    def put(self, key, data):               
        initial_position = self.hash(key)   # 초기 위치 (처음 해시 값)
        i = initial_position                 
        j = 0                                
        while True:                         
            if self.a[i] == None:           # 빈 곳을 발견
                self.a[i] = key             # 키는 해시테이블에
                self.d[i] = data            # data는 리스트 d에 저장
                return

            if self.a[i] == key:            # 이미 key가 해시테이블에 존재하면
                self.a[i] = data            # 데이터만 갱신
                return

            j += 1                               # 다음 원소 검사를 위해
            i = (initial_position + j) % self.M  # 다음 위치
            if i == initial_position:            # 계속 돌아도 빈 곳이 없어서 초기 위치로 돌아오면 탐색 실패
                break

    def get(self,key):                           
        initial_position = self.hash(key)        
        i = initial_position                     # 초기위치 i
        j = 1                                    # 다음 위치 탐색
        while self.a[i] != None:                 # 계속 탐색을 하기 위해서

            if self.a[i] == key:                 # 내가 찾는 애의 키랑 일치하면
                return self.d[i]                 # 탐색 성공

            i = (initial_position + j)% self.M   # a는 키값들의 집합이고 그 안의 원소들을 가리키는 index는 i
            j += 1
            if i == initial_position:
                return None
        return None

    def print_table(self):
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ',end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])),' ' ,end='')
        print()
        # for i in range(self.M):
        #     print('{:4}'.format(str(self.d[i])),' ' ,end='')

    def delete(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 1
        while self.a[i] != None:                 

            if self.a[i] == key:  
                self.a[i] == None
                self.d[i] == None
                self.N -= 1 
                return 

            i = (initial_position + j)% self.M   
            j += 1
            if i == initial_position:
                self.a[i] == None
                self.d[i] == None
                self.N -= 1 
                return None
        return None