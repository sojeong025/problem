'''
높이가 4 이하인 모든 지점이 물에 잠긴다 -> 잠기지 않은 안전구역이 몇 개냐
상하좌우 델타 탐색 : 행 탐색 하다가 4보다 크면 거기서부터 탐색 연결된 블럭이 얼마나 되는지 파악
* 조건 : 4보다 커야 뻗어나감
* 4, 5, 6 ... 다 검사해야하므로 지도 배열은 건들면 안되고 체크 배열 만들어야 함
'''
import sys
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y, h):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            continue
        if visited[nx][ny] == 0 and height[nx][ny] > h:
            DFS(nx, ny, h)

N = int(input())
cnt = 0
res = 0
height = [list(map(int, input().split())) for _ in range(N)]
for h in range(0,101):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and height[i][j] > h:
                cnt += 1
                DFS(i, j, h)
    res = max(res, cnt)
    if cnt == 0:
        break
print(res)
