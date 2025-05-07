from collections import deque

def BFS(N, M, graph):

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    que = deque()
    day = 0
    max_day = 0

    # 해당 문제의 핵심 ( 병렬 BFS )
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 :
                que.append([i,j,day])
    
    while que :
        now_i, now_j, day = que.popleft()

        for i in range(4) :
            next_i = now_i + dx[i]
            next_j = now_j + dy[i]

            if 0<= next_i <N and 0<= next_j < M :
                if graph[next_i][next_j] == 0 : 
                    que.append([next_i, next_j, day +1])
                    graph[next_i][next_j] = 1
                    max_day = max(max_day, day+1)


    for row in graph :
        if 0 in row :
            return -1
    
    return max_day




if __name__ == '__main__' :
    M, N = map(int,input().split())

    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))
    print(BFS(N, M, graph))