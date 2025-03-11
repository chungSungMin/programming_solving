def dfs(depth, now):
    global result
    if depth == M : 
        print(*result)
        return
    else :
        for i in range(now, N + 1):
            # if visited[i] == False :
            result.append(i)
            # visited[i] = True
            dfs(depth + 1, i + 1)
            result.pop()
            # visited[i] = False


if __name__ == '__main__':
    N, M = map(int, input().split())
    result = []
    # visited = [False] * (N + 1)
    dfs(0, 1)