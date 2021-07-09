import sys

sys.stdin = open("in3.txt", "r")
n = int(input())
dis = [[100] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dis[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dis[a][b] = 1
    dis[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

res = [0] * (n + 1)
score = 100
for i in range(1, n + 1):
    for j in range(1, n + 1):
        res[i] = max(res[i], dis[i][j])
    score = min(score, res[i])
cand = []
for i in range(1, n + 1):
    if res[i] == score:
        cand.append(i)

print(f'{score} {len(cand)}')
for x in cand:
    print(x, end = ' ')

