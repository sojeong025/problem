import sys
input = sys.stdin.readline

n = int(input())
pipe = [list(map(int, input().split())) for _ in range(n)]

# 0 가로 1 세로 2 대각선
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
# 첫 시작 위치 : 처음 파이프는 가로로 놓이며 파이프 끝이 (0, 1)에 위치함
dp[0][0][1] = 1


# 0번째 행은 가로로 오는 경우 밖에 없으므로 먼저 초기화 시켜줌
for i in range(2, n):
    if pipe[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for r in range(1, n):
    for c in range(1, n):
        # 현재 위치 대각선인 경우 : 수평, 수직 , 대각
        if pipe[r][c] == 0 and pipe[r][c-1] == 0 and pipe[r-1][c] == 0:
            dp[2][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]

        if pipe[r][c] == 0:
            # 현재 위치 가로인 경우 : 수평 , 대각
            dp[0][r][c] = dp[0][r][c-1] + dp[2][r][c-1]
            # 현재 위치 세로인 경우 : 수직 , 대각
            dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]

# 맨 마지막에 도착했을 때
print(sum(dp[i][n-1][n-1] for i in range(3)))