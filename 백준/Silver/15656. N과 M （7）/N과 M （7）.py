def dfs():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    else:
        for i in range(N):
            arr.append(lst[i])
            dfs()
            arr.pop()
        

N, M = map(int, input().split())
lst = map(int, input().split())
lst = sorted(lst)
arr = []
dfs()