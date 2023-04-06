import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(number, x, y):
    if len(number) == 7:
        result.add(number)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 > nx or nx >= 4 or 0 > ny or ny >= 4:
            continue
        else:
            dfs(number + arr[nx][ny], nx, ny)
    return


T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            dfs('', i, j)
    
    print(f'#{tc}', len(result))
