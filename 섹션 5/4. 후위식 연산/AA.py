import sys
#sys.stdin = open("in1.txt", "r")

a = input()

# 352+*9-
# +, -를 만나면 바로앞에 두개를 연산

stack = []
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    elif x == "+":
        stack.append(stack.pop() + stack.pop())
    elif x == "-":
        temp = stack.pop()
        stack.append(stack.pop()-temp)
    elif x == "*":
        stack.append(stack.pop() * stack.pop())
    elif x == "/":
        temp = stack.pop()
        stack.append(stack.pop() / temp)

print(stack[0])
