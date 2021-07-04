# 깊이 우선 탐색

import sys

# sys.stdin = open("input.txt", "r")


def dfs(v):
    if v > 7:
        return
    else:
        print(v, end=" ")
        dfs(v * 2)
        dfs(v * 2 + 1)


if __name__ == "__main__":
    dfs(1)
