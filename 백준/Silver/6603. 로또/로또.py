def dfs(result, depth, now):
    if depth == 6 :
        print(*result)
        return

    else :
        for i in range(now, K):
            # if depth + K - i < 6 :
            #     return
            # else :
            result.append(S[i])
            dfs(result, depth + 1, i + 1)
            result.pop()


if __name__ == '__main__':
    while True :
        test = list(map(int, input().split()))
        result = []
        if test[0] == 0 :
            break
        else :
            K = test[0]
            S = test[1 : ]
            dfs(result, 0,0)
            print()
