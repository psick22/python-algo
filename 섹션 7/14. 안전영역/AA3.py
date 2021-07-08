import sys
import copy
import time
sys.stdin = open("in4.txt", "r")
sys.setrecursionlimit(10**6)


def dfs(x, y, h):
    dm[x][y] = -1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx <= n - 1 and 0 <= ny <= n - 1:
            if dm[nx][ny] > h and dm[nx][ny] != -1:
                dfs(nx, ny, h)


if __name__ == '__main__':
    start = time.time()
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    mm = max(map(max, m))
    res = 0
    for z in range(mm):
        dm = copy.deepcopy(m)
        cnt = 0
        for i in range(n):
            for j in range(n):
                if dm[i][j] > z:
                    cnt += 1
                    dfs(i, j, z)
        res = max(res, cnt)
    print(res)
    print(time.time() - start)