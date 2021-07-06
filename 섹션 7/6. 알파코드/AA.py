import sys

sys.stdin = open("in3.txt", "r")


def dfs(L, res):
    global cnt
    if L == n or int(str[L]) == 0:
        s.add(res)
    else:
        if L == n - 1:
            dfs(L + 1, res + chr(int(str[L]) + 64))
        elif (int(str[L])==1 or int(str[L])==2) and int(str[L + 1]) == 0:
            dfs(L + 2, res + chr(int(str[L] + str[L + 1]) + 64))
        else:
            dfs(L + 1, res + chr(int(str[L]) + 64))
            if int(str[L]) == 1 or (int(str[L]) == 2 and int(str[L + 1]) < 7):
                dfs(L + 2, res + chr(int(str[L] + str[L + 1]) + 64))


if __name__ == "__main__":
    str = input()
    print(str)
    n = len(str)
    cnt = 0
    s = set()
    dfs(0, '')
    for x in s:
        print(x)
    print(len(s))

11+64