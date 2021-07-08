import sys

sys.stdin = open("in5.txt", "r")


def dfs(x, y, px, py):
    if x == 0:
        print(y)
    else:
        if x - px < 0:
            flag = False
            for k in range(3):
                if not flag:
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx <= 9 and 0 <= ny <= 9 and m[nx][ny] == 1:
                        flag = True
                        dfs(nx, ny, x, y)
        elif y - py != 0:
            ny_left = y - 1
            ny_right = y + 1
            if 0 <= ny_left <= 9 and 0 <= ny_right <= 9 and m[x][ny_left] == m[x][ny_right] == 1:
                if y - py > 0:
                    dfs(x, ny_right, x, y)
                else:
                    dfs(x, ny_left, x, y)
            else:
                flag = False
                for k in range(3):
                    if not flag:
                        nx = x + dx[::-1][k]
                        ny = y + dy[::-1][k]
                        if 0 <= nx <= 9 and 0 <= ny <= 9 and m[nx][ny] == 1:
                            flag = True
                            dfs(nx, ny, x, y)


if __name__ == "__main__":
    m = [list(map(int, input().split())) for _ in range(10)]
    dx = [0, 0, -1]
    dy = [-1, 1, 0]
    for i in range(10):
        if m[9][i] == 2:
            dfs(9, i, 0, 0)
