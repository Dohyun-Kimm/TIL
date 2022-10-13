
def bfs(v,N,t):
    visited = [0] * N + 1 # visited 생성
    q = []                  # q 생성
    q.append((v))           # 시작 정점 추가
    visited[v] = 1          # 방문정보 기록
    while q:
        v = q.pop(0)
        if v == t:          # visited(v)
            return 1        # 목표 발견
        # v에 인접하고 방문 안한 w 인큐하고, 표시하기
        for w in adjList[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
        return 0



T = 10
for t in range(T):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjList = [[] for _ in range(100)]
    for i in range(E):
        a, b = arr[i * 2], arr[i * 2 +1]
        adjList[a].append(b)

    print('#{} {}'.format(t+1, bfs(0, 99, 99)))     # 시작 정점, 마지막정점, 목표점