# bfs 연습하기
# 2022-08-25

# bfs 경로 출력

def bfs(G, v):      # G: 그래프,  v: 시작 지점
    visited = [0] * (N)   # n = 정점의 개수 방문 여부 표시
    queue = []              # 인접한 정점 인큐, 디큐하면서 방문
    queue.append(v)         # 시작 정점 v를 큐에 삽입
    while queue:            # 큐에 값이 있는 동안
        t = queue.pop(0)    # 디큐하고 t에 저장
        if not visited[t]:   # t를 방문 하지 않았다면
            visited[t] = 1
            print(t,end=' ')
            for i in G[t]:  # 정점 t와 인접한 정점들 오름차순
                queue.append(i) # i를 큐에 삽입
    

# 1 2 /1 3 /2 4 /2 5 /4 6 /5 6 /6 7 /3 7
''' graph = [
    [2, 3],
    [1, 4, 5],
    [1, 7],
    [2, 6],
    [2, 6],
    [4, 5, 7],
    [3, 6]
     ]
'''
V, E = map(int,input().split())
N = V + 1
graph = [[] for _ in range(N)]
for _ in range(N):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for q in range(N):
    print(graph[q])

bfs(graph,1)
