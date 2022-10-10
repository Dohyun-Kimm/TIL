# 이중배열 연습
# 2022-08-20

# 기본 함수 구현 하기
#  length
def length(iter):
    count  = 0
    for _ in iter:
        count +=1
    return count

def maxx(iter):
    m = iter[0]
    for x in iter:
        if x > m:
            m = x
    return m

def minn(iter):
    n = iter[0]
    for y in iter:
        if y < n:
            n = y
    return n

def summ(iter):
    total = 0
    for num in iter:
        total += num
    return total

def absol(int_n):
    if int_n <0:
        return -(int_n)
    else:
        return int_n

# 이중 배열 선언
N = 5
a = [[] * N for _ in range(N) ]
print(a)
b = [[0] * N for _ in range(N) ]
print(b)

# 이중 배열 채우기
for i in range(N):
    for j in range(N):
        a[i].append((j))            # 비어있는 리스트에 값 추가 하기
        b[i][j] = j                 # 0 으로 채운 리스트에 값 추가 하기
    print(a[i])

# 이중 배열 탐색

# 가로 탐색
for i in range(N):
    for j in range(N):
        print(a[i][j], end = '')              # 안쪽 루프 인덱스를 열에 넣기
print()
# 세로 탐색
for i in range(N):
    for j in range(N):
        print(b[j][i], end = '')              # 안쪽 루프 인덱스를 행에 넣기

print()
# 델타 탐색
c = [
    [1,0,0,1,0,0],
    [1,1,1,0,0,0],
    [0,1,0,1,0,1],
    [1,1,0,0,1,0],
    [0,0,0,1,1,0],
    [1,0,1,1,0,1],
]

# 방향키  우 하 좌 상 두개로 나눠서 만들기
di = [1,0,-1,0]                            # 우 좌
dj = [0,1,0,-1]                            # 상 하

N = length(c[0])
# 각 좌표를 중심으로 상하좌우에 1이 몇개 있지 카운트 하기
for i in range(N):
    for j in range(N):
        cnt = 0
        for d in range(4):                      # d ==0 일떄 우, d == 2 일때 좌
            x = i + di[d]
            y = j + dj[d]

            if -1 < x < N and -1 < y < N:
                # print(f'x;{x}, y:{y} c:{c[x][y]}')

                if c[x][y] ==1:
                    cnt += 1
        print(cnt, end=' ')
# 대각선 방향 까지 8방 카운트 하기

print()
di = [1,0,-1,0]                             # 우 좌
dj = [0,1,0,-1]                             # 상 하
dia = [[1,1], [1,-1], [-1,1], [-1,-1]]
# dia = [1,-1,-1,1]                           # 대각선
# dib = [1,1,-1,-1]
# for i in range(N):
#     for j in range(N):
#         cnt = 0
#         for d in range(4):
#             # (1,1) (-1,1) (-1,-1) (1,-1)
#             xx = i + dia[d]
#             yy = j + dib[d]
#
#             if -1<xx<N and -1<yy<N:
#                 print(f'({xx},{yy}) = {c[xx][yy]}')
#                 if c[xx][yy] ==1:
#
#                     cnt +=1
#         print(cnt)

# 1 칸 8방 서치 한번에
print()
for i in range(N):
    for j in range(N):
        cnt = 0
        for d in range(4):
            xx = i + dia[d][0]
            yy = j + dia[d][1]
            x = i + di[d]
            y = j + dj[d]
            if -1<x<N and -1<y<N :
                if c[x][y] == 1:
                    cnt +=1
            if -1<xx<N and -1<yy<N:
                if c[xx][yy] ==1:
                    cnt +=1

        print(cnt, end=' ')


# 다른 방법으로 8방 델타 서치
# dia dib 만들지 말고 한번에 dia = [[1,1], [1,-1], [-1,1], [-1,-1]]선언하기
# 대각선과 상하좌우는 따로따로 해주기

# n 칸  4방 서치 ==> 반복문을 하나 더 추가 해서 4방 + 길이 만큼 반복
# n = 2 일때

lp = [[1] * 5 for _ in range(5)]
n = 2
di = [[1, 2], [-1, -2], [0, 0],[0,0]]              # 상하
dj = [[0,0], [0,0], [1, 2], [-1, -2]]              # 좌우

dia = list()
for a in range(4):
    dia.append(list(map(int,range(1,3))))
print(dia)


i = 0
j = 4
count = 0
for q in range(5):
    print(lp[q])
print()
for k in range(4):              # 탐색 방향의 수 만큼 반복( 상하 좌우)
    for l in range(n):          # 각 방향마다 탐색해야하는 길이 만큼 반복
        x = i + di[k][l]
        y = j + dj[k][l]

        if -1 < x < 5 and -1 < y < 5:
            lp[x][y] += 1

for i in range(5):
    print(lp[i])







# n 칸 8방 서치

#
