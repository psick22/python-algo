import sys

sys.stdin = open("in5.txt", "r")


def dfs(L, sum, tsum):
    global max
    if sum + (total - tsum) < max:
        return

    if sum > limit:
        return

    if L == n:
        if sum > max:
            max = sum
    else:
        dfs(L + 1, sum + dogs[L], tsum + dogs[L])
        dfs(L + 1, sum, tsum + dogs[L])


if __name__ == "__main__":
    limit, n = map(int, input().split())
    dogs = [int(input()) for m in range(n)]
    total = sum(dogs)
    max = -2147000000
    dfs(0, 0, 0)
    print(max)
