import sys
input = sys.stdin.readline


def dfs(y, x, visited, lst, total):
    global result
    cnt = 0
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if 0 > nx or 0 > ny or nx >= C or ny >= R or graph[ny][nx] in lst or visited[ny][nx] == True:
            cnt += 1
        else:
            visited[ny][nx] = True
            lst.add(graph[ny][nx])

            dfs(ny, nx, visited, lst, total + 1)

            lst.remove(graph[ny][nx])
            visited[ny][nx] = False

    if cnt == 4:
        result = max(result, total)
        return result


R, C = map(int, input().split())

graph = []
for i in range(R):
    graph.append(list(input().strip()))



visited = [ [False] * C for _ in range(R)]
lst = set()
lst.add(graph[0][0])
result = 0
total = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

dfs(0, 0, visited, lst, total)
print(result)