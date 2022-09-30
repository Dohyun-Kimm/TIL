# 11724 연결 요소의 개수

def dfs(a):
    if visited[a] ==0:
        visited[a] =1
        for j in range(len(graph[a])):
            dfs(graph[a][j])
    else:
        return

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

visited = [0] *(N+1)
cnt =0
for i in range(1, len(visited)):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)
