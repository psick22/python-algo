import sys

# sys.stdin = open("in5.txt")


def check(num):
    cnt = 0
    for x in line:
        cnt += (x // num)
    return cnt


k, n = map(int, input().split())
line = []
res = 0
largest = 0
for _ in range(k):
    temp = int(input())
    line.append(temp)
    largest = max(largest, temp)

lt = 1
rt = largest

while lt <= rt:
    mid = (lt + rt) // 2
    if check(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
