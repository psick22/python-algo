import sys

sys.stdin = open("in5.txt", "r")


def dfs(x, y):
    if dy[x][y] != 0:
        return dy[x][y]

    if x == 0 and y == 0:
        return arr[0][0]
    else:

        if y == 0:
            dy[x][y] = arr[x][y] + dfs(x - 1, y)
        elif x == 0:
            dy[x][y] = arr[x][y] + dfs(x, y - 1)
        else:
            dy[x][y] = arr[x][y] + min(dfs(x - 1, y), dfs(x, y - 1))

        return dy[x][y]


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]
    print(dfs(n - 1, n - 1))
