import sys
sys.stdin = open('input.txt')



N = int(input())
M = int(input())

INF = int(1e8)
adjM = [[INF] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    adjM[i][i] = 0
for _ in range(M):
    s, e, w = map(int, input().split())
    adjM[s][e] = w

start , end = map(int, input().split())

print(start, end)