"""
맨 위 줄 1번째 칸부터 확인 > 두번째 줄에 되는 칸 있으면 세번째 줄
세번째 줄에 되는 칸 없으면 두번째 줄로 다시 올라가기
"""

import sys
sys.stdin = open('input.txt')


def check(r):
    for c in range(r):
        # 세로 체크
        if board[r] == board[c] or abs(board[r] - board[c]) == r - c:
            return 0
    return 1


def backtracking(r):
    global cnt
    # 마지막 행까지 다 돌았으면 횟수 증가
    if r == N: 
        cnt += 1
    else:
        for c in range(N):
            board[r] = c
            # 해당 자리에 놓을 수 있다면 다음 행으로
            if check(r):
                backtracking(r+1)



N = int(input())

# 몇번째 줄에 몇번째 칸에 있는지 체크
board = [0]*N
cnt = 0
backtracking(0)
print(cnt)