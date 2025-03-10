from collections import deque

def bfs(graph, visited, i, j):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    que = deque()
    que.append((i,j))
    visited[i][j] = True

    while que :
        i, j = que.popleft()
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]

            if 0 <= ni < N and 0<= nj < M :
                if graph[ni][nj] == 1 and visited[ni][nj] == False :
                    que.append((ni, nj))
                    visited[ni][nj] = True




if __name__ == '__main__':
    T = int(input())
    
    for _ in range(T):
        total = 0
        M , N, S = map(int,input().split())

        graph = [ [0] * M for _ in range(N)]
        visited = [ [False] * M for _ in range(N)]
        
        for i in range(S):
            col, row = map(int, input().split())
            graph[row][col] = 1
        
        
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 1 and visited[i][j] == False:
                    bfs(graph, visited, i, j)
                    total += 1

        print(total)