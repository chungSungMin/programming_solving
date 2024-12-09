from collections import deque

def bfs(x, y, n, visited):
    que = deque()
    que.append([x, 0])
    visited[x] = True
    
    if x == y:
        return 0
    
    while que:
        now, cnt = que.popleft()
        
        if now == y:
            return cnt
        
        next_add = now + n
        next_mul2 = now * 2
        next_mul3 = now * 3
        
        if next_add <= y and not visited[next_add]:
            visited[next_add] = True
            que.append([next_add, cnt + 1])
        
        if next_mul2 <= y and not visited[next_mul2]:
            visited[next_mul2] = True
            que.append([next_mul2, cnt + 1])
        
        if next_mul3 <= y and not visited[next_mul3]:
            visited[next_mul3] = True
            que.append([next_mul3, cnt + 1])
    
    return -1

def solution(x, y, n):
    visited = [False for _ in range(y + 1)]
    answer = bfs(x, y, n, visited)
    return answer