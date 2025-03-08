# 입력을 모두 받아준다.
# dy dx 로 이동 가능한 8개의 경로를 모두 설정한다
# 시작점에서 부터 BFS를 돌려서 원하는 위치 위의 거리를 계산한다.
from collections import deque

T = int(input())

dy = [2,2,-2,-2,1,-1,1,-1]
dx = [-1,1,1,-1,2,2,-2,-2]

def bfs(y, x):
    global graph
    queue = deque()
    graph[y][x] = 0
    queue.append((y, x))

    if y == end_y and x == end_x :
        print(0)
        return
    while queue:
        y, x = queue.popleft()
        for i in range(8):
            ny = dy[i] + y
            nx = dx[i] + x

            if 0 <= ny < N and 0<= nx < N :
                if ny == end_y and nx == end_x:
                    graph[ny][nx] = graph[y][x] + 1
                    print(graph[ny][nx])
                    return
                elif graph[ny][nx] == 0 :
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append((ny, nx))

for _ in range(T):
    N = int(input())
    graph = []
    for i in range(N):
        graph.append([0] * N)

    start_y, start_x = map(int, input().split())
    end_y , end_x = map(int, input().split())
    bfs(start_y, start_x)

