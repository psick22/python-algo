import sys

sys.stdin = open("in1.txt", "r")


def dfs(v):
    global cnt
    if v == n:
        for x in path:
            print(x, end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if g[v][i] != 0 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                dfs(i)
                path.pop()
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())

    g = [[0] * (n + 1) for _ in range(n + 1)]
    ch = [0] * (n + 1)

    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1

    cnt = 0
    ch[1] = 1
    path = [1]
    dfs(1)
    print(cnt)
