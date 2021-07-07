import sys

sys.stdin = open("in5.txt", "r")


def dfs(x, y):
    global cnt
    cnt += 1
    m[x][y] = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx <= n - 1 and 0 <= ny <= n - 1:
            if m[nx][ny] == 1:
                dfs(nx, ny)


if __name__ == "__main__":
    n = int(input())
    m = [list(map(int, input(''))) for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    res = []
    for i in range(n):
        for j in range(n):
            if m[i][j] == 1:
                cnt = 0
                dfs(i, j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)
