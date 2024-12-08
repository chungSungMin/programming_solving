import sys
from collections import deque
input = sys.stdin.readline


def bfs(row, col ,visited):
    que = deque()
    que.append([row, col, 1, 0])
    visited[0][row][col] = True
    if row == N-1 and col == M-1 :
        return 1

    while que:
        row, col, cnt, brk = que.popleft()
        if row == N-1 and col == M-1 :
            return cnt
        for i in range(4):
            next_row = row + dy[i] 
            next_col = col + dx[i]  

            if 0 <= next_row < N and 0 <= next_col < M :
                if visited[brk][next_row][next_col] == False and graph[next_row][next_col] == 0:
                    que.append([next_row, next_col, cnt + 1, brk])
                    visited[brk][next_row][next_col] = True

                if visited[brk][next_row][next_col] == False and graph[next_row][next_col] == 1 and brk == 0:
                    que.append([next_row, next_col, cnt+1, brk+1])
                    visited[brk][next_row][next_col] = True
    return -1


N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().strip())))
visited = [ [ [False for _ in range(M)] for _ in range(N)] for _ in range(2)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

print(bfs(0,0,visited))
