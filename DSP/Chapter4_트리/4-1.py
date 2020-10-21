class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

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

