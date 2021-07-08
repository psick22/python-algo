import sys

sys.stdin = open("in1.txt", "r")


def dfs(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
    else:
        if y - 1 >= 0 and ch[x][y - 1] == 0 and m[x][y - 1] == 1:
            dfs(x, y - 1)
        elif y + 1 <= 9 and ch[x][y + 1] == 0 and m[x][y + 1] == 1:
            dfs(x, y + 1)
        else:
            dfs(x - 1, y)


if __name__ == "__main__":
    m = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0] * 10 for _ in range(10)]
    for i in range(10):
        if m[9][i] == 2:
            dfs(9, i)
