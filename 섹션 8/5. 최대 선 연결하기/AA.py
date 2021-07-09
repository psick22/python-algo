import sys

sys.stdin = open("in5.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
dy = [0] * n
dy[0] = 1
res = 0

for i in range(1, n):
    max = 0
    for j in range(i - 1, 0, -1):
        if arr[i] > arr[j] and dy[j] > max:
            max = dy[j]
    dy[i] = max + 1
    if dy[i] > res:
        res = dy[i]

print(res)