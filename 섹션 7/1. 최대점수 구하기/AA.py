import sys

sys.stdin = open("in5.txt", "r")


def dfs(L, sum, time):
    global res

    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum

    else:

        dfs(L + 1, sum + score[L], time + times[L])
        dfs(L + 1, sum, time)


if __name__ == "__main__":
    n, m = map(int, input().split())
    score = []
    times = []
    for i in range(n):
        a, b = map(int, input().split())
        score.append(a)
        times.append(b)
    res = -2147000000
    dfs(0, 0, 0)
    print(res)
