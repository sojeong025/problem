import sys
sys.stdin = open('input.txt')

def dijkstra(s, V):
    U = [0] * (V+1)
    U[s] = 1
    for i in range(V+1):
        D[i] = adjM[s][i]

    N = V + 1
    for _ in range(N-1):
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                w = i
                minV = D[i]
        U[w] = 1
        for v in range(V+1):
            if 0 <= adjM[w][v] < INF:
                D[v] = min(D[v], D[w] + adjM[w][v])



N = int(input())
M = int(input())

INF = int(1e8)
adjM = [[INF] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    adjM[i][i] = 0
for _ in range(M):
    s, e, w = map(int, input().split())
    if adjM[s][e] >= w:
        adjM[s][e] = w

start , end = map(int, input().split())


D = [0] * (N+1)
dijkstra(start, end)
print(D[end])