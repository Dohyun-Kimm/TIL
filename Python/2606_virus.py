# 바이러스

def dfs(v):
    if not visited[v]:
        visited[v] += 1
        for w in range(len(nodes[v])):
            dfs(nodes[v][w])
    else:
        return


V = int(input())
E = int(input())
visited = [0] *(V+1)
nodes = [[] for _ in range(V+1)]
for i in range(E):
    a,b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
# print(nodes)

dfs(1)
print(sum(visited)-1)