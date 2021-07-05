import sys
import itertools as it

sys.stdin = open("in1.txt", "r")
n, f = map(int, input().split())
b = [1] * n
for i in range(1, n):
    b[i] = b[i - 1] * (n - i) / i
a = list(range(1, n + 1))

for temp in it.permutations(a):
    sum = 0
    for idx, value in enumerate(temp):
        sum += value * b[idx]
    if sum == f:
        for i in temp:
            print(i, end=' ')
        break
