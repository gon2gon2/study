def Lotto() :
    ball1 = ball2 = ball3 = ball4 = ball5 = ball6 = ball7 = 0
    ball1 = random.randint(1, 45)
    while True :
        ball2 = random.randint(1,45)
        ball3 = random.randint(1,45)
        ball4 = random.randint(1,45)
        ball5 = random.randint(1,45)
        ball6 = random.randint(1,45)
        if ball1 != ball2 != ball3 != ball4 != ball5 != ball6:
            break

    while True :
        ball7 = random.randint(1, 45)
        if ball7 != ball1 and ball7 != ball2 and ball7 != ball3 and ball7 != ball4 and ball7 != ball5 and ball7 != ball6 :
            break
    print(str(ball1) + ' ' + str(ball2) + ' ' + str(ball3) + ' ' + str(ball4) + ' ' + str(ball5) + ' ' + str(ball6))
    return ball7

import random
ball7 = Lotto()
print('Bonus number is ' + str(ball7))
