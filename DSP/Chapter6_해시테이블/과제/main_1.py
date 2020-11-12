from linear_prob import Linear_Probing
if __name__ == '__main__':
    t = Linear_Probing(13)
    t.put(25,'grape')
    t.put(37,'apple')
    t.put(18,'banana')
    t.put(55,'cherry')
    t.put(22,'mango')
    t.put(35,'lime')
    t.put(50,'orange')
    t.put(63,'watermelon')
    t.print_table()
    t.delete(35)
    t.print_table()