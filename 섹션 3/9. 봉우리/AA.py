import sys

sys.stdin = open("in5.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

## 가장자리 초기화
a.insert(0, [0] * n)
a.append([0] * n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if max(a[i][j - 1], a[i][j + 1], a[i - 1][j], a[i + 1][j]) < a[i][j]:
            cnt += 1
print(cnt)
