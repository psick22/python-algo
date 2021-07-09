import sys

sys.stdin = open("in5.txt", "r")


def dfs(L, s):
    global total_min
    if L == m:
        # 거리 계산
        case_sum_distance = 0
        for i in range(n):
            for j in range(n):
                if x[i][j] == 1:
                    temp_min = 2147000000
                    for p in res:
                        temp = abs(pizza[p][0] - i) + abs(pizza[p][1] - j)
                        if temp < temp_min:
                            temp_min = temp
                    case_sum_distance += temp_min

        if case_sum_distance < total_min:
            total_min = case_sum_distance
    else:
        for k in range(s, len(pizza)):
            res[L] = k
            dfs(L + 1, k + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    pizza = []
    for i in range(n):
        for j in range(n):
            if x[i][j] == 2:
                pizza.append((i, j))
    total_min = 2147000000
    res = [0] * m
    dfs(0, 0)
    print(total_min)
