class Quad_Probing:
    def __init__(self,size):
        self.M = size                # 해시테이블 크기
        self.a = [None] * size       # 키값들의 집합
        self.d = [None] * size       # 데이터의 집합
        self.N = 0                   # 원소의 개수

    def hash(self, key):
        return key % self.M          # 해시값 반환

    def put(self, key, data):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while True:
            if self.a[i] == None:
                self.a[i] = key
                self.d[i] = data
                self.N += 1
                return
            if self.a[i] == key:
                self.d[i] = data
                return
            j += 1
            i = (initial_position + j*j) % self.M
            if self.N > self.M:
                break
            
    def get(self,key):
        initial_position = self.hash(key)
        i = initial_position
        j = 1
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]
            i = (initial_position + j*j) % self.M
            j += 1
        return None

    def print_table(self):
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ',end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])),' ' ,end='')
        print()