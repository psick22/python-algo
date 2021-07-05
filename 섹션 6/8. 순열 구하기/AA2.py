import sys

sys.stdin = open("in5.txt", "r")


def dfs(L, ch, res):
    global cnt
    if L == m:
        for i in res:
            print(i, end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                res[L] = i
                ch[i] = 1
                dfs(L + 1, ch, res)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    # res = [0] * m
    cnt = 0
    # ch = [0] * (n + 1)
    dfs(0, [0] * (n + 1), [0] * m)
    print(cnt)
