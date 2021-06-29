import sys

# sys.stdin = open("in1.txt", "r")

# 키, 몸무게
# 키와 몸무게 중 적어도 하나는 다른 지원자보다 키가 크거나, 몸무게가 많이 나가는 지원자
# 키/ 몸무게 둘다 작거나
# 생각해볼 수 있는 방법
# 1. 키 - 내림차순 정렬 => 대상보다 키큰 사람과 몸무게 비교후 결정 => 이중for문?
# 2. 키 - 내림차순 정렬 => 키의 탐새갛면서 최대값 나올 때 마다 카운트
n = int(input())
arr = []
cnt = 0
largest = 0
for _ in range(n):
    height, weight = map(int, input().split())
    arr.append((height, weight))
    arr.sort(reverse=True)

for x, y in arr:
    if y > largest:
        largest = y
        cnt += 1

print(cnt)
