import random

is_playing = True


counts = 0  

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')
        
    answer = random.randint(1, 100)  # 1이상 100이하의 난수

    # 몇 번만에 정답을 맞혔는지 담는 변수

    T = int(input('1 이상 100 이하의 숫자를 입력하세요. :'))
    if T>100 and T<1:
        T=int(input('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.'))
    else:
        if T < answer:
            counts +=1
            print('UP!!!')
        else:
            
            if T ==answer:
                print(f'Correct!!! {counts} 만에 정답을 맞히셨습니다.\n')
                re = input('게임을 재시작하시려면 y, 종료하시려면 n을 입력하세요. :')
                if re =='n':
                    print('이용해주셔서 감사합니다. 게임을 종료합니다.')
                    break
                elif re =='y':
                    print('================================')
                    print('        Up and Down Game        ')
                    print('================================')
                
                    answer = random.randint(1, 100)  # 1이상 10000이하의 난수

                    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수
                else:
                    print('잘못된 값을 입력하셨습니다. 게임을 종료합니다.')
                    break
            else:
                counts +=1
                print('Down!!!')

