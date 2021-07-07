import sys
from collections import deque

# sys.stdin = open("in1.txt", "r")

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

dq = deque()

for i in range(n):
    for j in range(n):
        if m[i][j] == 1:
            m[i][j] = 0
            dq.append((i, j))
            while dq:
                temp = dq.popleft()
                for k in range(8):
                    x = temp[0] + dx[k]
                    y = temp[1] + dy[k]
                    if 0 <= x <= n - 1 and 0 <= y <= n - 1:
                        if m[x][y] == 1:
                            m[x][y] = 0
                            dq.append((x, y))
            cnt += 1
print(cnt)
