# 11724 연결 요소의 개수


# 리커션이 끝나지 않음
def dfs(a):
    visited[a] =1
    for j in graph[a]:
        if visited[j] ==0:
            visited[j] =1
            dfs(j)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]    # 노드 담을 공간

for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

visited = [0] *(N+1)                # 방문 여부 표시
cnt =0                              # 연결된곳 카운트
for i in range(1, len(visited)):
    if not visited[i]:
        dfs(i)
        cnt += 1
if M == 0:
    print(0)
else:
    print(cnt)
