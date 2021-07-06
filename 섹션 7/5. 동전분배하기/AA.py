import sys

# sys.stdin = open("in5.txt", "r")


def dfs(L):
    global res
    if L == n:
        if people[0] == people[1] or people[1] == people[2] or people[0] == people[2]:
            return
        temp = max(people) - min(people)
        if temp < res:
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
