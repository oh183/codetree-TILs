n, m = map(int, input().split())

r_list = [
    [] for _ in range(n + 1)
]

visited = [False for _ in range(n + 1)]
vertex_cnt = 0

for _ in range(m):
    start, end = map(int, input().split())
    r_list[start].append(end)
    r_list[end].append(start)

visited[1] = True

def dfs(vertex):
    global vertex_cnt
    for curr_v in r_list[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            vertex_cnt += 1
            dfs(curr_v)

dfs(1)

print(vertex_cnt)