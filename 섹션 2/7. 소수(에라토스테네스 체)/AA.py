import sys

sys.stdin = open("in2.txt", "r")
n = int(input())

count = 0
arr = [0]*(n+1)

for i in range(2, n+1):
    if arr[i] == 0:
        count += 1
        for j in range(i, n+1, i):
            arr[j] = 1

print(count)
