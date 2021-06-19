import sys

sys.stdin = open("in1.txt", "r")

arr = list(range(21))

for _ in range(10):
    start, end = map(int, input().split())
    for i in range((end - start + 1) // 2):
        arr[start + i], arr[end - i] = arr[end - i], arr[start + i]

arr.pop(0)
for x in arr:
    print(x, end=" ")
