def dfs(depth):
    global result
    if depth == M :
        print(*result)
        return
    else :
        for i in range(1, N + 1):
            if visited[i] == True :
                continue
            else :
                result.append(i)
                visited[i] = True
                dfs(depth + 1)
                result.pop()
                visited[i] = False


if __name__ == '__main__':
    N, M = map(int, input().split())
    result = []
    visited = [False] * (N + 1)
    dfs(0)