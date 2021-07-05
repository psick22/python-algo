import sys

sys.stdin = open("in5.txt", "r")


def dfs(L, s):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(s, n + 1):
            res[L] = i
            dfs(L + 1, i + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    dfs(0, 1)
    print(cnt)
