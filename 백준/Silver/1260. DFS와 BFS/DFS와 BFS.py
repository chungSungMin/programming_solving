from collections import deque

def bfs(graph, visited, start):
    que = deque()
    que.append(start)
    visited[start] = True

    while que :
        now_node = que.popleft()
        print(f'{now_node + 1}', end = ' ')
        for i in range(0, N) :
            if graph[now_node][i] == True and visited[i] == False :
                que.append(i)
                visited[i] = True

def dfs(graph, visited, start) :
    visited[start] = True
    print(f'{start + 1}', end = ' ')
    for i in range(0, N) :
        if graph[start][i] == True and visited[i] == False :
            dfs(graph, visited, i)


if __name__ == '__main__':
    N, R, S = list(map(int, input().split()))
    
    graph = [ [False] * N for i in range(N) ]
    visited = [False] * N

    for i in range(R):
        s, e = map(int, input().split())
        graph[s-1][e-1] = True
        graph[e-1][s-1] = True
    dfs(graph, visited, S-1)
    visited = [False] * N
    print()
    bfs(graph, visited, S-1)
