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

    print('전위순회:\t',end='')
    t.preorder(t.root)
    print('\n중위순회:\t',end='')
    t.inorder(t.root)
    print('\n후위순회:\t',end='')
    t.postorder(t.root)
    print()
    print(t.root.item)