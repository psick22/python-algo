import sys

#sys.stdin = open("in2.txt", "r")

n = int(input())
a = list(map(int, input().split()))
lp = 0
rp = n - 1
last = 0
res = ""
temp = []

while lp <= rp:
    if a[lp] > last:
        temp.append((a[lp], "L"))
    if a[rp] > last:
        temp.append((a[rp], "R"))
    temp.sort()


    if len(temp) == 0:
        break
    else:
        res += temp[0][1]
        last = temp[0][0]
        if temp[0][1] == "L":
            lp += 1
        else:
            rp -= 1
    temp.clear()
print(len(res))
print(res)