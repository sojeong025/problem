import sys
sys.stdin = open('input.txt')

# 오른쪽과 아래 탐색
dx = [0, 1]
dy = [1, 0]


def DFS(x, y):
    global res, min_sum
    if min_sum < res:
        return
    if x == n-1 and y == n-1:
        if min_sum > res:
            min_sum = res

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = 1
            res += arr[nx][ny]
            DFS(nx, ny)
            visited[nx][ny] = 0
            res -= arr[nx][ny]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 1000
    res = arr[0][0]
    visited = [[0] * n for _ in range(n)]
    DFS(0, 0)
    print(f'#{tc} {min_sum}')

