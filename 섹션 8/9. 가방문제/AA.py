import sys

sys.stdin = open("in1.txt", 'r')

n, limit, = map(int, input().split())
backs = []
for i in range(n):
    weight, price = map(int, input().split())
    backs.append((weight, price))

