from collections import deque

def bfs(graph, que):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while que :
        i,j,tm = que.popleft()

        if tm > -1 and graph[i][j] != 'F' and (i == R -1 or j == C - 1 or i == 0 or j == 0) :
            return tm + 1

        for k in range(4):
            ni = dx[k] + i
            nj = dy[k] + j

            if 0 <= ni < R and 0 <= nj < C and graph[ni][nj] != '#':

                if tm > -1 and graph[ni][nj] == '.':
                    graph[ni][nj] = '_'
                    que.append([ni, nj, tm+1])

                elif tm == -1 and graph[ni][nj] != 'F' :
                    graph[ni][nj] = 'F'
                    que.append([ni, nj, -1])

    return 'IMPOSSIBLE'


if __name__ == '__main__':
    R, C = map(int, input().split())
    graph = []
    for i in range(R):
        graph.append(list(input()))
        if 'J' in graph[i] :
            que = deque([[i, graph[i].index('J'), 0]])
    
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'F':
                que.append([i,j,-1])

    print(bfs(graph, que))
        


