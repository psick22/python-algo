import sys

sys.stdin = open("in5.txt", "r")


def dfs(L, s, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1

    else:
        for i in range(s, n):
            c[L] = a[i]
            dfs(L + 1, i + 1, sum + a[i])


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    c = [0] * k
    cnt = 0
    dfs(0, 0, 0)
    print(cnt)
