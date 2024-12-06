import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col, visited, rain):
    que = deque()
    que.append([row, col])
    visited[row][col] = True   

    while que:
        now_row, now_col = que.popleft()
        for i in range(4):
            next_row = now_row + dx[i]
            next_col = now_col + dy[i]

            if 0 <= next_col < N and 0 <= next_row < N :
                if graph[next_row][next_col] > rain  and visited[next_row][next_col] == False:
                    que.append([next_row, next_col])
                    visited[next_row][next_col] = True
    return visited

max_rain = -1
result = -1
N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))


dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(N):
    for j in range(N):
        if max_rain < graph[i][j] :
            max_rain = graph[i][j]

for i in range(max_rain):
    visited = [ [False for _ in range(N)] for _ in range(N)]
    count = 0
    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == False:
                visited = bfs(j,k,visited,i)
                count += 1
    if result < count :
        result = count
print(result)