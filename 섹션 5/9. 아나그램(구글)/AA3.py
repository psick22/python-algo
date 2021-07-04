import sys

sys.stdin = open("in4.txt")

a = input()
b = input()
# 아스키코드로 해싱 -> 해시테이블 구현 (리스트 해시)
# 대문자 65~ -> -65 -> 0~25
# 소문제 97~ -> -71 -> 26~51

str1 = [0] * 52
str2 = [0] * 52

for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1
    else:
        str1[ord(x) - 71] += 1

for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1
    else:
        str2[ord(x) - 71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")

