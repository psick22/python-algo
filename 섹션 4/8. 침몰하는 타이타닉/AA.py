import sys
from collections import deque
import time
sys.stdin = open("in3.txt", "r")
start_time = time.time()
n, m = map(int, input().split())
people = list(map(int, input().split()))
people.sort()
people = deque(people)
cnt = 0
while people:
    if len(people) == 1:
        cnt += 1
        break
    if people[0] + people[-1] > m:
        people.pop()
        cnt += 1
    else:
        people.popleft()
        people.pop()
        cnt += 1


end_time = time.time()
time = end_time - start_time

print(cnt)
print(f'수행 시간 : {time : .5f}')
