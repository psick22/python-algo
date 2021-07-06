import sys

sys.stdin = open("in5.txt", "r")


def dfs(L, sum, num):
    # if flag[sum] == 1:
    #     return
    if L == k:
        if sum < 0:
            return
        flag[sum] = 1
    else:
        for i in range(num, k):

            if ch[i] == 0:
                ch[i] = 1
                dfs(L + 1, sum + a[i], i)
                dfs(L + 1, sum - a[i], i)
                dfs(L + 1, sum, i)
                ch[i] = 0


if __name__ == "__main__":
    k = int(input())
    a = list(map(int, input().split()))
    ch = [0] * (k + 1)
    s = sum(a)
    flag = [0] * (s + 1)
    dfs(0, 0, 0)
    cnt = 0
    for i in flag:
        if i == 0:
            cnt += 1
    print(cnt)
