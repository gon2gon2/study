class Node:
    def __init__(self, key, value, left = None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.item = value


class BST:
    def __init__(self):         # 트리 생성자
        self.root = None 

    def get(self, key):         # 탐색 연산
        return self.get_item(self.root, key)

    def get_item(self, n, k):
        if n == None:
            return None

        if n.key > k:
            return self.get_item(n.left, k)

        elif n.key < k:
            return self.get_item(n.right, k)

        else:
            return n.value



    def put(self, key, value):  # 삽입 연산
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n == None:
            return Node(key, value)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)

        elif n.key < key:
            n.right = self.put_item(n.right, key, value)

        else:
            n.value = value

        return n


    def min(self):              # 최솟값 가진 노드 찾기
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, n):
        if n.left == None:
            return n
        return self.minimum(n.left)

    def delete_min(self):
        if self.root == None:
            print('트리가 비어 있음')
        self.root = self.del_min(self.root)

    def del_min(self,n):
        if n.left == None:
            return n.right
        n.left = self.del_min(n.left)
        return n






    def delete(self, k):
        self.root = self.del_node(self.root, k)
    
    def del_node(self, n ,k):
        if n == None:
            return None

        if n.key > k:
            n.left = self.del_node(n.left, k)
        
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








    def preorder(self, n):                 # 전위순회
        if n != None:
            print(str(n.item),' ',end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self, n):                  # 중위순회
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.item),' ',end='')    
            if n.right:
                self.inorder(n.right)

    def postorder(self, n):                 # 후위순회
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.item),' ',end='')

    def levelorder(self, root):             # 레벨순회
        q = []
        q.append(root)
        while len(q) != 0:
            t = q.pop()
            print(str(t.item), ' ',end='')
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)

    def height(self,root):
        if root == None:
            return 0
        return max(self.height(root.left),self.height(root.right)) + 1
