import sys
from collections import Counter
# sys.stdin = open("in3.txt")

a = input()
b = input()
res = Counter(a) - Counter(b)

if len(res) == 0:
    print("YES")
else:
    print("NO")

