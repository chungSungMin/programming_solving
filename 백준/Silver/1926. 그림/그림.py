import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col) :
    scale = 1
    queue = deque()
    queue.append([row, col])
    graph[row][col] = 0

    while queue :
        row, col = queue.popleft()
        for i in range(4):
            next_row = row + d_row[i]
            next_col = col + d_col[i]
            if 0 <= next_row < N and 0 <= next_col < M :
                if graph[next_row][next_col] == 1 :
                    graph[next_row][next_col] = 0
                    scale += 1
                    queue.append([next_row, next_col])
    return scale


N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

d_row = [0,0,1,-1]
d_col = [1,-1,0,0]

count = 0
result = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 :
            count +=1 
            result.append(bfs(i,j))

print(count)
print(max(result) if result != [] else 0)


