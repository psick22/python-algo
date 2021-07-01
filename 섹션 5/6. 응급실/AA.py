import sys

# sys.stdin = open("in2.txt", "r")
from collections import deque

n, m = map(int, input().split())
arr = [(i, v) for i, v in enumerate(list(map(int, input().split())))]
dq = deque(arr)

cnt = 0
while True:
    temp = dq.popleft()
    if any(temp[1] < x[1] for x in dq):
        dq.append(temp)

    else:
        cnt += 1
        if temp[0] == m:
            print(cnt)
            break
