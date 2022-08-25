# 재미있는 오셀로 게임
#  흑돌 = 1 백돌 = 2


# 뒤집는 작업
def flip(mat, w, v):
    # while 문 써서 0나오면 탈출
    # 놓은 자리와 일치하는 좌표 나올떄까지 반복
    # 0이아니고 stone과 다르다면 stone과 같게만들어주기
    global stone
    i = 1
    dx = [i, -i, 0, 0, i, -i, -i, i]  # 0~3 까지 4방 그 이후로는 대각선
    dy = [0, 0, i, -i, i, i, -i, -i]
    for d in range(8):  # 우, 좌, 하, 상, 우하, 우좌, 좌상, 우상
        x = w + dx[d]
        y = v + dy[d]
        # 한방향으로 쭉 가는 부분
        while True:
            if -1 < x < N and -1 < y < N:  # 인덱스 오류 방지
                if mat[x][y] == 0:  # 돌이 안 놓인 곳 볼필요 업슴
                    break
                elif mat[x][y] == stone and can == 1:    # 같은 색 스톤 나오면 탈출 다음 방향으로
                    # 돌 뒤집기 작업.
                    break
                elif mat[x][y] != stone:                # 다른 색 돌일경우
                    print('where')
                    can = 1
                    x += dx[d]                  # 다음칸
                    y += dy[d]
            else:
                break
    for q in range(N):
        print(mat[q])
    print()
    return mat


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = 2        # white
    board[N // 2 - 1][N // 2] = 1       # black
    board[N // 2][N // 2 - 1] = 1       # black
    board[N // 2][N // 2] = 2       # white
    for q in range(N):
        print(board[q])
    print()
    for m in range(M):
        # x y 돌
        a, b, stone = map(int, input().split())
        if board[a-1][b-1] == 0:
            board[a-1][b-1] = stone
        board = flip(board,a-1,b-1)

    # 게임이 끝난 후 돌의 개수 카운트
    countB = 0
    countW = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                countB += 1
            elif board[i][j] == 2:
                countW += 1

    print('#'+str(t+1), str(countB), str(countW))
