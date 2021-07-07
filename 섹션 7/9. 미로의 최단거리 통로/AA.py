import sys
from collections import deque

sys.stdin = open("in5.txt", "r")

m = [list(map(int, input().split())) for _ in range(7)]
dis = [[0] * 7 for _ in range(7)]
dq = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

m[0][0] = 1

dq.append((0, 0))
while dq:
    temp = dq.popleft()
    for i in range(4):
        x = temp[0] + dx[i]
        y = temp[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and m[x][y] == 0:
            m[x][y] = 1
            dis[x][y] = dis[temp[0]][temp[1]] + 1
            dq.append((x, y))
if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])
