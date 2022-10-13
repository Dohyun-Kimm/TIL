# 1961_숫자배열 회전
# 2022-08-25
# 1120: 1145, + 5mins

# 90도 180도 270도 회전시킨 모양을 출력하기
# 90도 돌리는 함수 만들기
# 함수를 3번 돌려서 각 함수 종료시 새로운 배열 리턴

def rotate(mat):
    return list(map(list,zip(*mat[::-1])))


T = int(input())    # number of test case
for t in range(T):
    N = int(input())    # size of array N*N
    matrix = list()
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    ninety = rotate(matrix)             # rotate 90 degree
    oneEighty = rotate(ninety)          # rotate 90 degree from ninety
    twoSeventy = rotate(oneEighty)      # rotate 270 degree
    
    # print format
    print('#{}'.format(t+1))
    for i in range(N):
        print('{} {} {}'.format(''.join(map(str,ninety[i])), ''.join(map(str,oneEighty[i])), ''.join(map(str,twoSeventy[i]))))
