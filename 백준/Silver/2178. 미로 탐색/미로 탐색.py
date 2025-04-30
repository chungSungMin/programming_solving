from collections import deque


def BFS(graph, visited):
    que = deque()
    que.append([0,0,1])
    visited[0][0] = True
    
    while que :
        now_i, now_j, cnt = que.popleft()
        for i in range(4):
            next_i = now_i + dx[i]
            next_j = now_j + dy[i]

            if 0<= next_i < N and 0<= next_j < M : 

                if next_i == N-1 and next_j == M-1 : 
                    return cnt + 1
                elif graph[next_i][next_j] == 1 and visited[next_i][next_j] == False : 
                    que.append([next_i, next_j, cnt+1])
                    visited[next_i][next_j] = True




if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int, input())))
    visited = [ [False] * M  for _ in range(N)]

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    print(BFS(graph, visited))