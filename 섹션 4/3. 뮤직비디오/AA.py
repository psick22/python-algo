import sys

sys.stdin = open("in5.txt", 'r')


def check(num):
    cnt = 0
    sum = 0
    for x in a:
        if sum + x > num:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt + 1


n, m = map(int, input().split())
a = list(map(int, input().split()))
longest = max(a)

lt = 1
rt = sum(a)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= longest and check(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
