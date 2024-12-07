import sys
from collections import deque
input = sys.stdin.readline


def bfs(visited, floor, row, col):
    que = deque()
    que.append([floor, row, col,0])
    visited[floor][row][col] = True

    while que:
        now_f, now_r, now_c, count = que.popleft()
        for i in range(6):
            next_f = now_f + d_l[i]
            next_r = now_r + d_r[i]
            next_c = now_c + d_c[i]

            if 0 <= next_f < L and 0<= next_r < R and 0<= next_c < C :
                if graph[next_f][next_r][next_c] == '.' and visited[next_f][next_r][next_c] == False :
                    visited[next_f][next_r][next_c] = True
                    que.append([next_f, next_r, next_c, count + 1])
                elif graph[next_f][next_r][next_c] == 'E':
                    return count + 1
    return -1


while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break

    graph = []  
    for _ in range(L): 
        sub_graph = [] 
        for _ in range(R): 
            line = input().strip()
            sub_graph.append(list(line)) 
        graph.append(sub_graph)  
        input().strip()

    visited = [[ [ False for _ in range(C)] for _ in range(R) ] for _ in range(L)]

    d_l = [1,-1,0,0,0,0]
    d_r = [0,0,1,-1,0,0]
    d_c = [0,0,0,0,1,-1]

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if graph[i][j][k] == 'S' :
                    result = bfs(visited, i, j, k)
    if result > 0 :
        print(f'Escaped in {result} minute(s).')
    
    else :
        print('Trapped!')


