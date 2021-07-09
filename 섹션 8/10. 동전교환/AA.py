import sys

# sys.stdin = open("in1.txt", "r")

n = int(input())
coins = list(map(int, input().split()))
m = int(input())

dy = [1000] * (m + 1)
dy[0] = 0

for i in range(n):
    for j in range(coins[i], m + 1):
        dy[j] = min(dy[j - coins[i]] + 1, dy[j])

print(dy[m])
