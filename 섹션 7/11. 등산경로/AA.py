import sys

sys.stdin = open("in5.txt", "r")


def dfs(x, y):
    global cnt
    if x == end[0] and y == end[1]:
        cnt += 1
    else:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if m[nx][ny] > m[x][y]:
                    dfs(nx, ny)


if __name__ == "__main__":
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    start = (0, 0, 2147000000)
    end = (0, 0, -2147000000)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if m[i][j] < start[2]:
                start = (i, j, m[i][j])
            if m[i][j] > end[2]:
                end = (i, j, m[i][j])

    dfs(start[0], start[1])
    print(cnt)