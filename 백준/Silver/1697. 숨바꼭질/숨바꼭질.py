from collections import deque


def BFS(N, K):
    que = deque()
    que.append(N)

    while que :
        now_index = que.popleft()

        if 0 <= now_index -1 <= 100000 :
            if now_index - 1 == K :
                return graph[now_index] + 1
            
            elif graph[now_index-1] == 0 :
                que.append(now_index-1)
                graph[now_index-1] = graph[now_index] + 1
        

        if 0 <= now_index + 1 <= 100000 :
            if now_index + 1 == K :
                return graph[now_index] + 1
            
            elif graph[now_index + 1] == 0 :
                que.append(now_index + 1)
                graph[now_index+1] = graph[now_index] + 1

        if 0 <= now_index * 2 <= 100000 :
            if now_index * 2 == K :
                return graph[now_index] + 1
            
            elif graph[now_index * 2] == 0 :
                que.append(now_index * 2)
                graph[now_index * 2] = graph[now_index] + 1




if __name__ == '__main__':
    N, K = map(int, input().split())
    graph = [0] * 100001

    if N == K :
        print(0)
    else:
        print(BFS(N,K))