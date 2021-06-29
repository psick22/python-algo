import sys
import time
start_time = time.time()

sys.stdin = open("in5.txt", "r")
n, m = map(int, input().split())
people = list(map(int, input().split()))
people.sort(reverse=True)
cnt = 0
lp = 0
rp = n - 1

while lp <= rp:
    if people[lp] + people[rp] > m:
        lp += 1
        cnt += 1
    else:
        lp += 1
        rp -= 1
        cnt += 1

end_time = time.time()
time = end_time - start_time
print(cnt)

print(f'수행 시간 : {time : .5f}')
