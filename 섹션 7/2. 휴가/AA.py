import sys

sys.stdin = open("in5.txt", "r")


def dfs(L, sum):
    global res
    if L == n:
        if sum > res:
            res = sum
    else:
        if L + T[L] <= n:
            dfs(L + T[L], sum + P[L])
        dfs(L + 1, sum)


if __name__ == "__main__":
    n = int(input())
    T = []
    P = []
    for i in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)
    res = -2147000000
    dfs(0, 0)
    print(res)
