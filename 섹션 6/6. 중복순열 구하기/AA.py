import sys

sys.stdin = open("in5.txt", "r")


def dfs(L):
    global cnt
    if L == m:
        cnt += 1
        for i in res:
            print(i, end=' ')
        print()
        pass

    else:
        for i in range(1, n + 1):
            res[L] = i
            dfs(L + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    dfs(0)
    print(cnt)
