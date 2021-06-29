import sys

# sys.stdin = open("in1.txt", "r")

# m 회 높이 조정 이후 가장 높은 곳 - 가장 낮은 곳 출력


l = int(input())
arr = list(map(int, input().split()))
m = int(input())

# arr 내림차순으로 정렬
arr.sort(reverse=True)

for _ in range(m):
    arr[0] -= 1
    arr[l - 1] += 1
    if arr[0] < arr[1] or arr[l-1] > arr[l-2]:
        arr.sort(reverse=True)

print(arr[0] - arr[l - 1])