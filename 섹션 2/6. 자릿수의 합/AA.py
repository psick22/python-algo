import sys

sys.stdin = open("in1.txt", "r")
n = int(input())
a = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum


def digit_sum2(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum


max = -2147000000
for i in a:
    total = digit_sum(i)
    if total > max:
        max = total
        res = i

print(res)
