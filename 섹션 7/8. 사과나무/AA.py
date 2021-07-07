import sys
from collections import deque

sys.stdin = open("in5.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
sum = 0
dq = deque()
ch[n // 2][n // 2] = 1
sum += a[n // 2][n // 2]
dq.append((n // 2, n // 2))
L = 0
while True:
    if L == n // 2:
        break
    size = len(dq)
    for i in range(size):
        temp = dq.popleft()
        for j in range(4):
            x = temp[0] + dx[j]
            y = temp[1] + dy[j]
            if ch[x][y] == 0:
                sum += a[x][y]
                dq.append((x, y))
                ch[x][y] = 1
    L += 1

print(sum)
