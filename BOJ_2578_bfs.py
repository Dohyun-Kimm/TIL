# BOJ_2578 빙고
# 2022-08-28

# 빙고가 3개가 되면 이기는 게임
# 몇번째 수를 부르고 빙고를 외치게 되는지.

# 1~5 빙고판에 써져 있는 숫자
# 6~ 10 사회자가 부르는 숫자

bingo_board = list()
check_board = [[0] * 5 for _ in range(5)]  # 빙고판 숫자 불린 위치 기록


def bfs(v, n):  # v= 시작 지점 , n = 찾으려는 숫자
    global check_board
    global bingo_board
    visited = [[0] * 5 for _ in range(5)]
    queue = list()
    queue.append(v)
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, 1, -1, -1]
    while queue:
        t = queue.pop(0)  # 인덱스 값 입력 받았기 때문에 -1 할 필요 없음
        if not visited[t[0]][t[1]]:
            visited[t[0]][t[1]] = 1
        for d in range(8):  # 8방향 델타 탐색
            x = t[0] + dx[d]
            y = t[1] + dy[d]
            if -1 < x < 5 and -1 < y < 5:  # x,y가 좌표안에 있다면
                if bingo_board[x][y] == n:  # 찾으려는 숫자를 찾았을경 우
                    check_board[x][y] = 1  # 해당하는 위치에 표시해줌 나중에 빙고 탐색에 쓰임
                    return
                else:
                    queue.append([x, y])  # 리스트 형태로 입력해주어야함. 첫째노드 입력 받은것 처럼
        # print(visited)


def search(mat):
    cnt_bingo = 0
    for a in range(5):
        row_count = 0
        for b in range(5):
            if mat[a][b] == 1:
                row_count += 1
        if row_count == 5:
            cnt_bingo += 1
    for a in range(5):
        col_count = 0
        dia_count = 0
        adia_count = 0
        for b in range(5):
            if mat[b][a] == 1:
                col_count += 1
            if mat[a][a] == 1:
                dia_count = 1
            if mat[a][4 - a] == 1:
                adia_count += 1
        if col_count == 5:
            cnt_bingo += 1
        if dia_count == 5:
            cnt_bingo += 1
        if adia_count == 5:
            cnt_bingo += 1
    return cnt_bingo


# 빙고판 입력 받기
for _ in range(5):
    line = list(map(int, input().split()))
    bingo_board.append(line)
# print(bingo_board)
# 사회자가 부르는 빙고 번호 입력 받기
count = 0  # 사회자가 몇번째 수를 불렀는지 카운트
for i in range(5):
    nums = list(map(int, input().split()))
    for j in range(5):
        count += 1
        bfs([2, 2], nums[j])  # BFS로 들어온 숫자 찾기
        cnt = search(check_board)
        if cnt == 3:
            print(count)
            print(check_board)
            break
