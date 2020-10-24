# def binary_search(left,right, t):
#     if left > right: return Node
#     mid = (left + right) // 2
#     if a[mid]==t: return Node
#     if a[mid] > t: binary_search(left,mid-1,t)
#     else: binary_search(mid+1,right, t)



a = [1,2,3,4,5,6,7,8,9,10]

def b_search(lst, left=None, right= None,target):
    
    n = len(lst)//2
    
    
    if lst[n]== t: return n
    l_lst = lst[:n]
    r_lst = lst[n:]

    if l_lst[-1] < t: return b_search(l_lst, t)
    else: return b_search(r_lst, t)

b_search(a,3)