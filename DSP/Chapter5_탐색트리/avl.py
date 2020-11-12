class Node:
    def __init__(self, key, value, height, left = None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right

class AVL:
    def __init__(self):
        self.root = None

    def height(self, n):
        if n == None:
            return 0
        return n.height

    def put(self,key,value):
        self.root= self.put_item(self.root, key, vlaue)

    def put_item(self, n, key, value):
        if n == None:
            return Node(key, value, 1)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value
            return n
        
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)
    
    def balance(self,n):
        if self.bf(n) > 1:
            if self.bf(n.left) < 0:
                n.left = self.rotate_left(n.left)
            n = self.rotate_right(n)
        
        elif self.bf(n) < -1:
            if self.bf(n.right) > 0:
                n.right = self.rotate_right(n.right)
            n = self.rotate_left(n)
        return n

    def bf(self, n):
        return self.height(n.left) - self.height(n.right)

    def rotate_right(self,n):
        x= n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def rotate_left(self, n):
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right)) +1
        x.height = max(self.height(x.left), self.height(x.right)) +1
        return x
    def delete(self, k):
        self.root = self.del_node(self.root,k)
    def del_node(self,n,k):
        if n== None:
            return None
        if n.key > k:
            n.left = sel.fdel_node(n.left, k)
        elif n.key < k:
            n.right = self.del_node(n.right, k)
        
        else:
            if n.right == None:
                return n.left
            if n.left == None:
                return n.right
            target = n
            n = self.minimum(target.right)
            n.right = self.del_min(target.right)
            n.left = target.left
        return n


    def delete_min(self):
        if self.root == None:
            print('트리가 비어 있음')
        self.root = self.del_min(self.root)

    def del_min(self, n):
        if n.left == None:
            return n.right
        n.left = self.del_min(n.left)
        return n

    def min(self):
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self,n):
        if n.left == None:
            return n
        return self.minimum(n.left)