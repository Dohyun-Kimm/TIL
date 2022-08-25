# IM 대비 모의 시험
# 과수원
# 제약사항 5< N < 100
# 2< p < 100  + , x
# each cell 0< virus <100

# max function
def bigger(m, n):
    if m > n:
        return m
    else:
        return n


T = int(input())
for t in range(T):
    N, p = map(int, input().split())
    mat = list()  # 과수원 크기
    for _ in range(N):
        mat.append(list(map(int, input().split())))
    # 풀이 방법 및 제약 사항
    # 8방 델타 탐색 인덱스가 벗어나면 계산하지 않게 해야 오류안남
    # 모든 셀에 대하여 한번씩 돌면서 max값 찾기
    # delta 리스트 만들기 각 셀마다 1 부터 p까지 들어가야함

    dx = [list(range(1, p + 1)), list(range(-1, -p - 1, -1)), [0]*p, [0]*p]  # 우 좌
    dy = [[0] * p, [0] * p, list(range(1, p + 1)), list(range(-1, -p - 1, -1))]  # 하 상
    # +1 +1 -1 -1
    diagonalX = [
        list(range(1, p + 1)),
        list(range(1, p + 1)),
        list(range(-1, -p - 1, -1)),
        list(range(-1, -p - 1, -1))
    ]

    # +1 -1 -1 +1
    diagonalY = [
        list(range(1, p + 1)),
        list(range(-1, -p - 1, -1)),
        list(range(-1, -p - 1, -1)),
        list(range(1, p + 1))
    ]
    # print('dY: ', dy)
    # 대각선 좌표 (+1,+1), (+1,-1), (-1,-1), (-1,+1)
    max_virus = 0
    for i in range(N):
        for j in range(N):
            temp_sum_ten = mat[i][j]
            temp_sum_diag = mat[i][j]
            for a in range(4):  # length of delta list
                for b in range(p):  # p의 사거리 만큼 반복을 더 해야한다.
                    # print('a:', a, 'b:', b, dy[a][b])
                    x = i + dx[a][b]
                    y = j + dy[a][b]
                    diaX = i + diagonalX[a][b]
                    diaY = j + diagonalY[a][b]
                    if -1 < x < N and -1 < y < N:  # 조건을 만족하면 박멸 수 구하기
                        temp_sum_ten += mat[x][y]
                    if -1 < diaX < N and -1 < diaY < N:  # 조건을 만족하면 박멸 수 구하기
                        temp_sum_diag += mat[diaX][diaY]
            # 사거리 반복문, 방향 반복문이 다끝나면 그 좌표에 대한 박멸 결과가 나온다.
            big = bigger(temp_sum_diag, temp_sum_ten)
            if big > max_virus:
                max_virus = big
                # 완전 탐색이 끝나고 남온 결과가 1회 사격에 최대 박멸 수
    print('#' + str(t + 1), str(max_virus))
