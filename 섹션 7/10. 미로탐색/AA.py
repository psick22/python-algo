import sys

sys.stdin = open("in5.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            m[x][y] = 1
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 6 and 0 <= ny <= 6 and m[nx][ny] == 0:
                dfs(nx, ny)
            m[x][y] = 0


if __name__ == "__main__":
    m = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    m[0][0] = 1
    dfs(0, 0)
    print(cnt)
