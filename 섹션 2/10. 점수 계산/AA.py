import sys

sys.stdin = open("in3.txt", "r")
n = int(input())
answer = list(map(int, input().split()))

combo = 1
score = 0
for i in answer:
    if i == 1:
        score += combo
        combo += 1
    else:
        combo = 1

print(score)