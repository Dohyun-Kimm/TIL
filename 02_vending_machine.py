print('=================================')
print('         Vending Machine         ')
print('=================================')
print('[Menu]')
print('1. 콜라 500원')
print('2. 사이다 700원')
print('3. 레모네이드 4500원')
print('4. 오렌지주스 2000원')
print('5. 초코우유 1200원')
print('6. 아메리카노 3600원')
print('=================================')

menus = ['콜라', '사이다', '레모네이드', '오렌지주스', '초코우유', '아메리카노']  # 메뉴 이름
costs = [500, 700, 4500, 2000, 1200, 3600]  # 메뉴 가격
# 자판기에 넣은 총 누적 금액
menu_cost = dict(zip(costs,menus))
print(menu_cost)
total =0  
while True:
    print()
    money = int(input('금액을 넣어주세요.(그만 넣으시려면 0을 입력하세요.) : '))
    
    if money<0:
        print('금액은 1원 이상 넣어주세요.')      
    elif money == 0:
        break
    else:
        total +=money
    print(f'현재 누적 금액은 {total}입니다.')
    
if total < 500:
    print(f'{total}원으로 구매 가능한 메뉴가 없습니다.')
else :
    print(f'{total}원으로 구매 가능한 메뉴는 다음과 같습니다.')
    #key = 가격 
    for idx,key in enumerate(menu_cost.keys(),start=1):
        can_buy =dict()
        can#
        if key <total:
            print(f'{idx} {menu_cost[key]} {key}원')
            can_buy[idx].append(key)
    to_buy= int(input('구매하실 메뉴의 번호를 입력하세요.'))
    # canbuy ={1: 500,...}

    if to_buy not in can_buy.keys():
        print('구매할 수 없는 메뉴입니다.')
    else:
        #menu_cost = dict(zip(costs,menus))
        print(f'{menu_cost[can_buy[to_buy]]}을/를 구매하셨습니다.')
        print(f'거스름돈은 {total-can_buy[to_buy]}원입니다. 감사합니다.')
