import sys
from collections import deque

sys.stdin = open("in4.txt", "r")

n, m = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(m)]
ch = [[0] * n for _ in range(m)]
dq = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
res = 0
for i in range(m):
    for j in range(n):
        if x[i][j] == 1:
            dq.append((i, j))
while dq:
    for i in range(len(dq)):
        temp = dq.popleft()
        for k in range(4):
            nx = temp[0] + dx[k]
            ny = temp[1] + dy[k]
            if 0 <= nx <= m - 1 and 0 <= ny <= n - 1 and x[nx][ny] == 0:
                x[nx][ny] = 1
                dq.append((nx, ny))
                ch[nx][ny] = ch[temp[0]][temp[1]] + 1
flag = 1
for i in range(m):
    for j in range(n):
        if x[i][j] == 0:
            flag = -1
if flag == 1:
    res = max(map(max, x))
    print(res)
else:
    print(-1)
