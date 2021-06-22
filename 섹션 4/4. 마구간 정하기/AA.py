import sys

sys.stdin = open("in5.txt", "r")


def check(num):
    cnt = 1
    last = a[0]
    for i in range(1, n):
        if a[i] - last >= num:
            cnt += 1
            last = a[i]
    return cnt


n, c = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort()
lt = 1
rt = a[n - 1]
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if check(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
