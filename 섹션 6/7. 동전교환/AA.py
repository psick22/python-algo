import sys

sys.stdin = open("in4.txt", "r")


def dfs(L, sum):
    global res

    if L > res:
        return
    if sum > m:
        return
    if sum == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            dfs(L + 1, sum + type[i])


if __name__ == "__main__":
    n = int(input())
    type = list(map(int, input().split()))
    m = int(input())
    type.sort(reverse=True)
    res = 2147000000
    dfs(0, 0)
    print(res)
