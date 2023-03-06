import sys
sys.stdin = open('9490_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flower = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for si in range(N):
        for sj in range(M):
            cnt = flower[si][sj]
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                for mul in range(1, flower[si][sj]+1):
                    ni, nj = si+di*mul, sj+dj*mul
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += flower[ni][nj]
            ans = max(ans, cnt)
    print(f'#{tc} {ans}')

