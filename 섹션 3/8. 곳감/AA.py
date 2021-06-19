import sys

sys.stdin = open("in5.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    row, dir, num = map(int, input().split())
    temp = [0 for _ in range(n)]
    for j in range(n):
        if dir == 0:
            x = a[row - 1][j]
            if j - num <= -n:
                temp[j - num + (n * (abs(j - num) // n))] = x
            else:
                temp[j - num] = x
        else:
            x = a[row - 1][j]
            if j + num >= n:
                temp[j + num - (n * (abs(j + num) // n))] = x
            else:
                temp[j + num] = x
    a[row - 1] = temp

res = s = 0
e = n

for i in range(n):
    for j in range(s, e):
        res += a[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)
