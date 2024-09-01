import heapq
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
jew = []
for i in range(N):
    mass, price = map(int,input().split())
    heapq.heappush(jew, (mass, price))

bags = []
for i in range(K):
    bags.append(int(input()))
bags = sorted(bags)

ans = 0
temp = []
for bag in bags:
    while jew and bag >= jew[0][0]:
        heapq.heappush(temp, -heapq.heappop(jew)[1])
    if temp:
        ans -= heapq.heappop(temp)
    elif not jew:
        break

print(ans)

    