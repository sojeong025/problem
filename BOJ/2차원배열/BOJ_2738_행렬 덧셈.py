N, M = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(N)]
b = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        a[i][j] += b[i][j]

for i in a:
    print(*i)