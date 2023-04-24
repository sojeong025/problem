import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline

from collections import deque

def bfs():
    q = deque([0, 0])
    melt = deque([])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cheeze = []
cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

