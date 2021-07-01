import sys

sys.stdin = open("in3.txt", "r")

a = input()
cnt = 0
size = 0
stack = []
for x in a:
    if x == "(":
        stack.append(x)
        size += 1
    else:  # ")"
        if stack[-1] == "(":
            stack.pop()
            stack.append("|")
            size -= 1
            cnt += size

        elif stack[-1] == "|":
            while stack[-1] == "|":
                stack.pop()
            cnt += 1
            stack.pop()
            size -= 1


print(stack)
print(cnt)