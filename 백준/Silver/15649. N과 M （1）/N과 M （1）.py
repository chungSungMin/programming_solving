
def dfs(result, N, M):
    if len(result) == M :
        print(*result)
        return
    else :
        for i in range(1, N + 1):
            if visited[i] :
                continue
            else :
                result.append(i)
                visited[i] = True
                dfs(result, N, M)
                result.pop()
                visited[i] = False


if __name__ == '__main__':
    N, M = map(int, input().split())
    result = []
    visited = [False] * ( N + 1)
    dfs(result, N, M)