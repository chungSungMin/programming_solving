import sys
from collections import deque
input = sys.stdin.readline

def bfs(max_idx, start_idx, target_idx, btn, visited):
    que = deque()
    if start_idx == target_idx :
        return 0
    que.append((start_idx, 0))
    visited[start_idx] = True

    while que:
        now_idx, count = que.popleft()
        if now_idx == target_idx:
            return count
        for i in range(2):
            next_idx = now_idx + btn[i]
            if 1 <= next_idx <= max_idx and not visited[next_idx] :
                que.append((next_idx, count + 1))
                visited[next_idx] = True
       
    return -1


F, S , G, U, D = map(int, input().split())
btn = [U, -1 * D]
visited = [False] * (F + 1)

result = bfs(F, S, G, btn, visited)
if result == -1 :
    print('use the stairs')
else :
    print(result)
