import sys

#sys.stdin = open("in4.txt", "r")


def dfs(L, sum):
    global cnt
    if sum > T:
        return
    if L == k:
        if sum == T:
            cnt += 1
    else:
        for j in range(N[L] + 1):
            dfs(L + 1, sum + j * C[L])


if __name__ == "__main__":
    T = int(input())
    k = int(input())
    C = []
    N = []
    cnt = 0
    for i in range(k):
        a, b = map(int, input().split())
        C.append(a)
        N.append(b)
    dfs(0, 0)
    print(cnt)