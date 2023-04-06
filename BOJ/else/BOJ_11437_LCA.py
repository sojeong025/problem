import sys
sys.stdin = open('input.txt')

N = int(input())
arr = []
maxN = 0
for _ in range(N-1):
    x, y = map(int, input().split())
    arr.append([x, y])
    maxN = max(maxN, max([x, y]))
    

