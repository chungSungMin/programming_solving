
def dfs(depth):
    if depth == M :
        global result
        global lst
        print(*result)
        return
    else :
        for i in range(0, N) :
            if not visited[i] :
                result.append(lst[i])
                visited[i] = True
                dfs(depth + 1)
                result.pop()
                visited[i] = False


if __name__ == '__main__':
    N, M = map(int,input().split())
    result = []
    visited = [False] * N
    lst = sorted(list(map(int, input().split())))
    dfs(0)
    