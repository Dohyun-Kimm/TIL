# 활주로 건설하기
# 2022-08-25
# 1325 -
# 활주로 건설하기
'''
경사로 높이 :1, 길이: x
가로또는 세로 방향
경사로를 설치 할 수 있는 조건: 높이의 차가 1이면서  2칸이상 차지하고있어야함
(2,2,3), (1,1,2), (2,1,1),(3,2,2)
경사로를 설치하는 방법
    - 경사로가 들어갈 좌표의 값에 0.5를 더해준다. 
만약 어떤 행의 모든 값이 차이가 1 이하라면 활주로 설치 가능 
'''
def len(a):
    count = 0
    for _ in a:
        count += 1
    return count

def abs(b):
    if b > 0:
        return b
    else:
        return -b

def numOfAirstrip(area):
    # if [i][j] - [i][j-1] >abs(1): break
    # elif [i][j] - [i][j-3] >= abs(2) : break
    # elif [i][j] - [i][j-1] <= abs(1) and 
    # [i][j-1] == [i][j-2]       
    # --> [i][j-1], [i][j-2] += 0.5
    # if i == N-1 : count +=1
    
    
    # find whether runway can be put
    

    # 2.evaluate wheter airstrip can be constructed
    # [i][j] - [i][j-1] <=1 for all coor in row -> count +=1
    count =0        #number of airstrips

    # row search for runways
    for i in range(N):
        for j in range(2, N):
            if abs(area[i][j] - area[i][j-1]) >1: break
            elif abs(area[i][j] - area[i][j-3]) >= 2: break
            elif abs(area[i][j] - area[i][j-1]) >1 and area[i][j-1] == area[i][j-2]:
                area[i][j-1] += 0.5
                area[i][j-2] += 0.5
            elif j == N-1:
                count += 1
    
    # column search for runways
    for i in range(N):
        for j in range(2, N):
            if abs(area[j][i] - area[j-1][i]) >1: break
            # 여기서 부터 i j 위치 바꿔주고 이미 경사로 설치된 구역 스킵하는 코드 추가 해야함
            elif abs(area[i][j] - area[i][j-3]) >= 2: break
            elif abs(area[i][j] - area[i][j-1]) >1 and area[i][j-1] == area[i][j-2]:
                area[i][j-1] += 0.5
                area[i][j-2] += 0.5
            elif j == N-1:
                count += 1




T = int(input())                    # Number of test case 
for t in range(T):
    N, X = map(int,input().split())     # N*N: area, X:length of runway
    airstrip = list()
    for _ in range(N):
        airstrip.append(list(map(int,input().split())))

    print('#{} {}'.format(t+1,numOfAirstrip(airstrip)))


