import sys

sys.stdin = open("in2.txt", "r")

a = input()
res = ''
stack = []

for x in a:
    if x.isdecimal():
        res += x
    else:
        if x == "(":
            stack.append(x)
        elif x == "*" or x == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                res += stack.pop()
            stack.append(x)
        elif x == "+" or x == "-":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.append(x)
        elif x == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()

# for i in range(len(a))a:
#     if a[i] == "+" or a[i] == "-" or a[i] == "(":
#         stack.append(a[i])
#     elif a[i] == "*" or a[i] == "/":
#         if len(stack) == 0:
#             res.append(a[i])
#             break
#         if stack[-1] == "+" or stack[-1] == "-":
#             stack.append(a[i])
#         else:
#             res.append(a[i])
#     elif a[i] == ")":
#         if len(stack) == 0:
#             res.append(a[i])
#             break
#         while stack[-1] != "(":
#             res.append(stack.pop())
#         stack.pop()
#     else:
#         res.append(a[i])
#
# while len(stack) != 0:
#     res.append(stack[-1])

print(res)
