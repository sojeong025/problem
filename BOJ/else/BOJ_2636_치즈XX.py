'''
녹일 수 있는 치즈를 찾기
=> 치즈를 시작으로 하면 찾기 힘들어짐
=> 공기에서 탐색 시작

(0,0) 시작으로 완전 탐색 -> 녹을 치즈는 또 다시 새로운 공기가 됨
-> 또다시 완전 탐색 이런 과정을 반복
'''


# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

from collections import deque

def bfs():
    q = deque([(0, 0)])
    melt_cheeze = deque([])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                # 공기면 계속 탐색하기 위해 q에 append
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                # 치즈면 한 번에 녹이기 위해 melt_cheeze에 append
                elif graph[nx][ny] == 1:
                    melt_cheeze.append((nx, ny))

    for x, y in melt_cheeze:
        graph[x][y] = 0
    return len(melt_cheeze)

n, m = map(int, input().split())
graph = []
cheeze = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    cheeze += sum(graph[i])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 1
while True:
    visited = [[0] * m for _ in range(n)]
    melt_cz = bfs()
    cheeze -= melt_cz
    if cheeze == 0:
        print(time, melt_cz, sep='\n')
        break
    time += 1


