import sys

sys.stdin = open("in1.txt", "r")


def dfs(x):
    if x == 0:
        return
    else:
        dfs(x//2)
        print(x % 2, end='')



if __name__ == "__main__":
    n = int(input())
    dfs(n)
