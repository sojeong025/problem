import sys
sys.stdin = open('input.txt')

# N 민초마을의 크기 M 초기체력 H 민초 마시고 증가하는 체력
N, M, H = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * N for _ in range(N)]
mint_cnt = 0
mint_eat = 0


def DFS(x, y, start, depth):
    global M, mint_cnt, mint_eat
    if map[x][y] == 1 and not start:
        mint_cnt = max(mint_cnt, mint_eat)
        if mint_cnt == mint:
            print(mint_cnt)
            exit(0)
        return
    if M == 0:
        return
    start = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= -1 or nx >= N or ny <= -1 or ny >= N:
            continue
        if visited[nx][ny]:
            continue
        if map[nx][ny] == 2:
            M += H
            mint_eat += 1

        M -= 1
        visited[nx][ny] = 1
        DFS(nx, ny, start, depth + 1)
        visited[nx][ny] = 0

        if map[nx][ny] == 2:
            M -= H
            mint_eat -= 1
        M += 1

    if depth == 0:
        print(mint_cnt)


home_x, home_y = -1, -1
mint = 0

for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            home_x, home_y = i, j
        if map[i][j] == 2:
            mint += 1
DFS(home_x, home_y, 1, 0)
