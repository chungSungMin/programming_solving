def dfs(result, lst, now,N):
    global cnt
    if result == S and now:
        cnt += 1

    for i in range(now, N) :
        result += lst[i]
        dfs(result, lst, i + 1, N)
        result -= lst[i]


if __name__ == '__main__' : 
    cnt = 0
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = sorted(lst)
    result = 0
    dfs(result,lst, 0, N)
    print(cnt)