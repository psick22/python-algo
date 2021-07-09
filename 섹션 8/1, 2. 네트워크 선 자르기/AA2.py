import sys

sys.stdin = open("in5.txt", "r")


def dfs(L):
    if dy[L] > 0:
        return dy[L]
    if L == 1 or L == 2:
        return L
    else:
        dy[L] = dfs(L - 1) + dfs(L - 2)
        return dy[L]


if __name__ == "__main__":
    n = int(input())
    dy = [0] * (n + 1)
    print(dfs(n))
