# 단지 번호 붙이기

def dfs(x,y):
    global house
    if mat[x][y]:
        mat[x][y] =0
        house +=1
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            if -1< xx< N and -1 < yy< N:
                dfs(xx, yy)
    else:
        return




# delta
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
mat = [[]*N for _ in range(N)]
# print(mat)
cnt =0                              # 단지수 카운트
cnt_list= list()                    # 단지별 주택 카운트
for i in range(N):
    mat[i]=list(map(int, input()))
# print(mat)


for i in range(N):
    for j in range(N):
        if mat[i][j]:
            house = 0
            dfs(i,j)
            cnt +=1
            cnt_list.append(house)

print(cnt)
cnt_list.sort()
for k in range(len(cnt_list)):
    print(cnt_list[k])
'''
7
1110101
0110101
1110101
0000111
0100000
0111110
0111001
{4 1 8 9 9}

7
1110011
1110011
1110011
0000011
0000000
0111100
0111000
{3 7 8 9}
'''