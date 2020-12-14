# (list를 이용한 버전)을 빨간 물음표 자리를 채워서 완성하고 해당 코드와 코드를 실행한 결과를 1개의 메모장(.txt)에 저장 제출

import random
balls = [ 0, 0, 0, 0, 0, 0, 0 ]
number = 0
results = ''

while number < 7:
    while True :
        pick = random.randint(1, 45)
        if pick not in balls:
            balls[number] = pick
            break
    number = number + 1
    results = results + str(pick) + ' '
print(results)