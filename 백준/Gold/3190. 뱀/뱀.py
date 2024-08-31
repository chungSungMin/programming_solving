import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
# 기본 0, 뱀 1, 사과 2 로 설정한다.
graph = [ [0] * N for _ in range(N)]



# 사과의 위치를 그래프에 표시합니다.
M = int(input())
for i in range(M):
    y, x = map(int, input().split())
    # 문제의 index는 1부터 시작이기 때문에 1을 제거한다.
    graph[y-1][x-1] = 2


# 명령어를 딕셔너리 형태로 저장합니다. 
K = int(input())
op = dict()
for i in range(K):
    time, method = input().split()
    op[int(time)] = method


# 순서대로 우, 하, 좌 상 설정한다 
dx = [1,0,-1,0]
dy = [0,1,0,-1]

cnt = 0 # 시간을 나타내는 변수.
que = deque() # 뱀의 길이와 위치를 설정하기 위한 deque()
que.append((0,0)) # 뱀의 시작 지점을 큐에 넣어둔다.
graph[0][0] = 1
direct = 0 # dx[0],dy[0] 이 오른쪽 이동이기에 초기화 한다.
x,y = 0, 0 # 뱀의 위치 초기화.


def turn(operation):
    global direct
    if operation == 'L':
        direct = (direct - 1) % 4
    elif operation =='D':
        direct = (direct + 1) % 4


while True:
    cnt += 1
    x += dx[direct]
    y += dy[direct]

    # 가장 먼저 종료 조건을 설정한다.
    # 벽을 벗어나는 경우
    if x < 0 or y < 0 or x >= N or y >= N :
        break

    # 머리가 몸에 닿는경우
    elif graph[y][x] == 1 :
        break

    # 사과가 있는 경우
    elif graph[y][x] == 2 :
        graph[y][x] = 1
        que.append((y,x))
        # 만약 방향 전환 하는 시간이라면 해당 명령어를 turn 함수에 넘겨준다.
        if cnt in op:
            turn(op[cnt])        

    # 단순히 전진하는 경우
    else :
        graph[y][x] = 1
        que.append((y,x))
        # 꼬리는 이동하기 떄문에 그래프에서 없애주는 처리를 진행한다.
        py, px = que.popleft()
        graph[py][px] = 0 
        # 만약 방향 전환 하는 시간이라면 명령어를 turn 함수에 넘겨준다.
        if cnt in op :
            turn(op[cnt])
print(cnt)


