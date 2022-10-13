# BOJ_2578 빙고
# 2022-08-28

# 빙고가 3개가 되면 이기는 게임
# 몇번째 수를 부르고 빙고를 외치게 되는지.

# 1~5 빙고판에 써져 있는 숫자
# 6~ 10 사회자가 부르는 숫자

def row_search(r_mat):
    row_bingo = 0
    for r in range(len(r_mat)):
        row_cnt = 0
        for rc in range(len(r_mat)):
            if r_mat[r][rc] == -1:
                row_cnt += 1
        if row_cnt == 5:
            row_bingo += 1
    return row_bingo


def col_search(c_mat):
    col_bingo = 0
    for c in range(len(c_mat)):
        col_cnt = 0
        for cr in range(len(c_mat)):
            # 만약 빙고판에 -1이 적혀있다면 호명된 번호의 위치임으로 카운트해줌
            if c_mat[cr][c] == -1:
                col_cnt += 1
        # 한 열이 전부다 호명된것이라면 카운트는 5가 되어야한다.
        # 빙고하나가 완성 되었다는 의미
        if col_cnt == 5:
            col_bingo += 1
    # 빙고의 수르 반환.
    return col_bingo


def dia_search(d_mat):
    dia_bingo = 0
    dia_cnt = 0
    rev_dia_cnt = 0
    for dia in range(len(d_mat)):
        if d_mat[dia][dia] == -1:
            dia_cnt += 1
        if d_mat[dia][4 - dia] == -1:
            rev_dia_cnt += 1
    if dia_cnt == 5:
        dia_bingo += 1
    if rev_dia_cnt == 5:
        dia_bingo += 1
    return dia_bingo


bingo_board = list()
# 빙고판 입력 받기
for _ in range(5):
    line = list(map(int, input().split()))
    bingo_board.append(line)
# print(bingo_board)
# 사회자가 부르는 빙고 번호 입력 받기
count = 0  # 사회자가 몇번째 수를 불렀는지 카운트
three_bingo = 0
found = 0
for i in range(5):  # 부르는 빙고번호의 행
    nums = list(map(int, input().split()))
    for j in range(5):  # 행에 있는 번호 호출, 빙고판에 표시하기
        for m in range(5):  # bingo board row search
            for n in range(5):  # bingo board col search
                # 빙고판 서치
                numberOfBingo = 0
                if nums[j] == bingo_board[m][n]:
                    # bingo board에서 호명된 숫자 찾고 bingo_board에서 지우기
                    bingo_board[m][n] = -1  # 지웠다는표시
                    count += 1
                # 여기서부터 빙고 3개인지 확인
                numberOfBingo += row_search(bingo_board) + col_search(bingo_board) + dia_search(bingo_board)
                # print(count, numberOfBingo)
                if numberOfBingo > 2:
                    # 3빙고 찾은 시점에서 몇개를 불렀는지 카운트하고 three_bingo에 저장
                    three_bingo = count
                    found = 1
                    break
            if found:
                break
        if found:
            break
    if found:
        break

print(three_bingo)
