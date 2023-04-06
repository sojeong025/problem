import sys
sys.stdin = open('input.txt')

def dfs(kcal, n, score, j):
    global result
    
    if kcal >= L:
        return
    if n > N:
        return
    if score >= result:
        result = score
    
    for i in range(j, N):
        score += lst[i][0]
        kcal += lst[i][1]
        dfs(kcal, n+1, score, i+1)
        score -= lst[i][0]
        kcal -= lst[i][1]


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())

    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))

    result = 0
    dfs(0, 0, 0, 0)

    print(f'#{tc} {result}')