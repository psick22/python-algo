import sys
import itertools as it

sys.stdin = open("in5.txt", "r")
n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0

for comb in it.combinations(a, k):

    if sum(comb) % m == 0:
        cnt += 1

print(cnt)
