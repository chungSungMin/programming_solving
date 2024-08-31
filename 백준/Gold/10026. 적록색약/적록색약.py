import sys
from collections import deque
import copy
input = sys.stdin.readline


def bfs(y, x, visited, graph):
    que = deque()
    que.append([y,x])
    visited[y][x] = True

    while que:
        ny, nx = que.popleft()
        for i in range(4):
            y = ny + dy[i]
            x = nx + dx[i]

            if 0 <= x < N and 0 <= y < N :
                if visited[y][x] == False:
                    if graph[y][x] == graph[ny][nx]:
                        visited[y][x] = True
                        que.append([y,x])

    

N = int(input())
graph1 = []

for i in range(N):
    graph1.append(list(input().strip()))

graph2 = copy.deepcopy(graph1)
for i in range(N):
    for j in range(N):
        if graph2[i][j] == 'G':
            graph2[i][j] = 'R'



# 이후 방문처리를 위해서 설정해준다. (1은 정상인, 2는 적록색약)
visited1 = [ [False] * N for _ in range(N)]
visited2 = [ [False] * N for _ in range(N)]


dx = [0,0,1,-1]
dy = [1,-1,0,0]


total1 = 0
total2 = 0
# 그래프에서 방문하지 않은 곳이 있다면 방문하게 된다.
for i in range(N):
    for j in range(N):
        if visited1[i][j] == False :
            bfs(i,j, visited1, graph1)
            total1 += 1
        if visited2[i][j] == False :
            bfs(i,j, visited2, graph2)
            total2 += 1


print(total1, total2)