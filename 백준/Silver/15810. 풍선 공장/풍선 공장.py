import sys
input = sys.stdin.readline

N, M = map(int, input().split())
stp = list(map(int, input().split()))

max_time = max(stp)
max_period = max_time * M  # 가장 오래걸리는 시간으로 제한을 해버린다.
start = 1 
end = max_period

def letsgo(stp, start, end):
    answer = end
    while start <= end:
        mid = (start + end) // 2
        total = sum(mid // time for time in stp)
        if total >= M:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer

print(letsgo(stp, start, end))