import sys

sys.stdin = open("in5.txt", "r")
str = input()

res = 0
for char in str:
    if char.isdecimal():
        res = res * 10 + int(char)
print(res)

cnt = 0

for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1
print(cnt)
