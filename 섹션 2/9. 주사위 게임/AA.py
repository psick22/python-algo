import sys

sys.stdin = open("in5.txt", "r")
n = int(input())
res = 0
for i in range(n):
    temp = input().split()
    temp.sort()
    a, b, c = map(int, temp)

    if a == b and b == c:
        money = 10000 + a * 1000
    elif a == b or a == c:
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + b * 100
    else:
        money = c * 100

    if money > res:
        res = money
print(res)
