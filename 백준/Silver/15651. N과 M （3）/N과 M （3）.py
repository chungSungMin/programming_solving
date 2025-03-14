def dfs():
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
    else:
        for i in range(1, N + 1):
            ans.append(i)
            dfs()
            ans.pop()

N, M = map(int, input().split())
visited = [False] * ( N  + 1)
ans = []
dfs()
