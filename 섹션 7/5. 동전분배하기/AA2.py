import sys

sys.stdin = open("in3.txt", "r")


def dfs(L):
    global res
    if L == n:
        temp = max(people) - min(people)
        if temp < res:
            s = set()
            for x in people:
                s.add(x)
            if len(s) == 3:
                res = temp

    else:
        for j in range(3):
            people[j] += coins[L]
            dfs(L + 1)
            people[j] -= coins[L]


if __name__ == "__main__":
    n = int(input())
    people = [0] * 3
    coins = []
    for i in range(n):
        coins.append(int(input()))
    res = 2147000000
    dfs(0)
    print(res)
