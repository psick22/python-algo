import sys

# sys.stdin = open("in5.txt", "r")

n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1

for i in range(n - 1):
    word = input()
    p[word] = 0

for key, value in p.items():
    if value == 1:
        print(key)
        break
