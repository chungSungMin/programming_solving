import sys

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))

dp = {}


def dfs(now, visitied):
    if visitied == (1 << N) - 1 :
        if graph[now][0] != 0 :
            return graph[now][0]
        else :
            return int(1e9)
        
    if (now, visitied) in dp:
        return(dp[(now, visitied)])
    
    min_cost = int(1e9)
    for next in range(1, N):
        if graph[now][next] == 0:
            continue
        if visitied & ( 1 << next) == 1 << next :
            continue
        cost = dfs(next, visitied | (1 << next)) + graph[now][next]
        min_cost = min(min_cost, cost)
    dp[((now, visitied))] = min_cost
    return min_cost

print(dfs(0, 1))