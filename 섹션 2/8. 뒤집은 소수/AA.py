import sys

sys.stdin = open("in2.txt", "r")
n = int(input())
arr = list(map(int, input().split()))


def reverse(num):
    res = 0
    while num > 0:
        remain = num % 10
        res = res * 10 + remain
        num = num // 10
    return res


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    else:
        return True


for i in arr:
    reversed = reverse(i)
    bool = is_prime(reversed)

    if bool:
        print(reversed)
