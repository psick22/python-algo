import sys

sys.stdin = open("in5.txt", "r")

a = input()
cnt = 0
stack = []

for i in range(len(a)):
    if a[i] == "(":
        stack.append(a[i])
    else:
        if a[i - 1] == "(":
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)

