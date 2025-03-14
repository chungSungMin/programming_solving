
def dfs(depth,now):
    global result
    if depth == M :
        print(*result)
        return
    else:
        for i in range(now, N + 1):
            result.append(i)
            dfs(depth + 1, i)
            result.pop()
    

if __name__ == '__main__':
    N, M = map(int,input().split())
    result = []
    dfs(0, 1)