from dlist_search import DList
if __name__ == '__main__':
    s = DList()
    s.insert_after(s.head, 'apple')
    s.insert_before(s.tail, 'orange')
    s.insert_before(s.tail, 'cherry')
    s.insert_after(s.head.next, 'pear')
    # s.print_list()
    # s.search('pear')