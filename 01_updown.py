import random

is_playing = True


  

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')
        
    answer = random.randint(1, 100)  # 1이상 100이하의 난수

    # 몇 번만에 정답을 맞혔는지 담는 변수
    counts = 0  
    while True:
        T = int(input('1 이상 100 이하의 숫자를 입력하세요. :'))
        if T >=1 and T<=100:
            if T > answer:
                counts +=1
                print('Down!!!')
            elif T < answer:
                counts +=1
                print(' Up!!!')
            else:
                print(f'Correct!!! {counts}회 만에 정답을 맞히셨습니다.\n')
                re =input('게임을 재시작하시려면 y, 종료하시려면 n을 입력하세요')
                if re =='y':
                    break
                elif re =='n':
                    print('이용해주셔서 감사합니다. 게임을 종료합니다.')
                    is_playing=False
                    break
                else:
                    print('잘못된 값을 입력하셨습니다. 게임을 종료합니다.')
        else:
            print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.')
            break