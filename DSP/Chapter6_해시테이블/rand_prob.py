import random
class RandProbing:
    def __init__(self,size):
        self.M = size
        self.a = [None] * size
        self.d = [None] * size
        self.N = 0

    def hash(self, key):
        return key % self.M
    
    def put(self,size):
        initial_position = self.hash(key)
        i = initial_position
        random.seed(1000)
