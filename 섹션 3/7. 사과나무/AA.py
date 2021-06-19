import sys

sys.stdin = open("in2.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

center = n // 2
sum = 0
for i in range(n):
    if i < center:
        for j in range(n):
            if center - i <= j <= center + i:
                sum += a[i][j]

    elif i == center:
        for j in range(n):
            sum += a[i][j]

    else:
        for j in range(n):
            if center - (n - (i + 1)) <= j <= center + (n - (i + 1)):
                sum += a[i][j]

print(sum)
