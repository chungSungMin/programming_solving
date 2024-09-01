num = int(input())
wall = 1
cnt = 1

while num > wall:
    wall += 6 * cnt
    cnt += 1

print(cnt)