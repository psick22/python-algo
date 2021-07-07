import sys

sys.stdin = open("in4.txt", "r")


def dfs(L, res):
    global cnt
    if L == n:
        print(res)
        cnt += 1
    else:
        for i in range(1, 27):
            if i == s[L]:
                dfs(L + 1, res + chr(i + 64))
            elif i >= 10 and s[L] == i // 10 and s[L + 1] == i % 10:
                dfs(L + 2, res + chr(i + 64))


if __name__ == "__main__":
    s = list(map(int, input()))
    n = len(s)
    s.append(-1)
    cnt = 0
    dfs(0, '')
    print(cnt)
