from itertools import combinations

def dfs(depth) :
    global cnt
    if depth == 15 :
        cnt = 1
        for sub in res :
            if sub.count(0) != 3:
                cnt = 0 
                break
        return
    
    g1, g2 = games[depth]
    for x,y in ((2,0), (1,1), (0,2)) : # g1 입장에서 패, 무, 승
        if res[g1][x] > 0 and res[g2][y] > 0 :
            res[g1][x] -= 1
            res[g2][y] -= 1
            dfs(depth + 1)
            res[g1][x] += 1
            res[g2][y] += 1



games = list(combinations(range(6), 2))
ans = []
for _ in range(4):
    lst = list(map(int, input().split()))
    res = [lst[i : i + 3] for i in range(0, 16, 3)]
    cnt = 0
    dfs(0)
    ans.append(cnt)
print(*ans)
    

