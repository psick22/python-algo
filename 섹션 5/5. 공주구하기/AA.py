import sys
from collections import deque

n, k = map(int, input().split())

dq = deque(list(range(1, n+1)))

while len(dq) > 1:
    for j in range(k):
        if j == k-1:
            dq.popleft()
        else:
            dq.append(dq.popleft())


print(dq[0])


