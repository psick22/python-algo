import sys

sys.stdin = open("in3.txt", "r")


def dfs(L, rem, cnt):
    global min
    if L == n:
        if rem == 0:
            if cnt < min:
                min = cnt

    else:
        val = rem // type[L]

        dfs(L + 1, rem % type[L], cnt + val)


if __name__ == "__main__":
    n = int(input())
    type = list(map(int, input().split()))
    rem = int(input())
    type.sort(reverse=True)
    min = 2147000000
    dfs(0, rem, 0)
    print(min)
