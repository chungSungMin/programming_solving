
def dfs(depth, now_idx):
    if depth == M :
        global result
        global lst
        print(*result)
        return
    else :
        for i in range(now_idx, N) :
            result.append(lst[i])
            dfs(depth + 1, i)
            result.pop()


if __name__ == '__main__':
    N, M = map(int,input().split())
    result = []
    lst = sorted(list(map(int, input().split())))
    dfs(0, 0)