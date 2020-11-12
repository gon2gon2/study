# root > left왼쪽 서브트리에 있는 노드들의 키 값들보다 큼
# root < right  노드 n의 키 값이 n의 오른쪽 서브트리에 있는 노드들의 키 값들보다 작음

# 전위 순회로 n을 root로 저장해놓고 계속 비교하면 될듯
from bst_hw import BST
if __name__=='__main__':
    t = BST()
    t.put(500,'apple')
    t.put(600,'banana')
    t.put(200,'melon')
    t.put(100,'orange')
    t.put(400,'lime')
    t.put(550,'kiwi')
    t.put(800,'grape')

def check_key(n, root):
    if n == None:
        return n
    if n.left and n.left.key < root.key:
        print(n.left.key,'<',root.key)
        return check_key(n.left,root)
    else:
        print('이진탐색트리 아님')


    if n.right and n.rigt.key > root.key:
        print(root.key,'<',n.right.key)
        return check_key(n.right, root)
    else:
        print('이진탐색트리 아님')
    
    

def bst_check(tree):
    rt = tree.root
    check_key(rt,rt)
    
bst_check(t)