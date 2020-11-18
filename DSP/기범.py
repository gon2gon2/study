def Lotto() :
    ball1 = ball2 = ball3 = ball4 = ball5 = ball6 = ball7 = 0
    ball1 = random.randint(1, 45)
    while True :
        ball2 = random.randint(1,45)
        if ball2 == ball1:
            continue
        
        ball3 = random.randint(1,45)
        if ball3 == ball2 and ball3 == ball1:
            continue

        ball4 = random.randint(1,45)
        if ball4 == ball2 and ball4 == ball1 and ball4 == ball3:
            continue

        ball5 = random.randint(1,45)
        if ball5 == ball2 and ball5 == ball1 and ball5 == ball3 and ball5 == ball4:
            continue

        ball6 = random.randint(1,45)
        if ball6 == ball2 and ball6 == ball1 and ball6 == ball3 and ball6 == ball4 and ball6 == ball5:
            continue


    while True :
        ball7 = random.randint(1, 45)
        if ball7 != ball1 and ball7 != ball2 and ball7 != ball3 and ball7 != ball4 and ball7 != ball5 and ball7 != ball6 :
            break
    print(str(ball1) + ' ' + str(ball2) + ' ' + str(ball3) + ' ' + str(ball4) + ' ' + str(ball5) + ' ' + str(ball6))
    return ball7

import random
# def Lotto() :
# …
# …
# return ball7
ball7 = Lotto()
print('Bonus number is ' + str(ball7))