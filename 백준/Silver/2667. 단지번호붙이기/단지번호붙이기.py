from collections import deque
import sys
# input = sys.stdin.readline


def bfs(graph, r, c):
    queue = deque()
    queue.append([r,c])
    graph[r][c] = 0
    count = 1

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]

            if 0 <= nr < N and 0 <= nc < N :
                if graph[nr][nc] == 1 :
                    queue.append([nr, nc])
                    graph[nr][nc] = 0
                    count +=1 
    return count


if __name__ == '__main__':
    N = int(input())
    graph = []
    result = []
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for i in range(N):
        graph.append(list(map(int, input())))

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 :
                result.append(bfs(graph, i, j))

    result = sorted(result)            
    print(len(result))
    for i in range(len(result)):
        print(result[i])