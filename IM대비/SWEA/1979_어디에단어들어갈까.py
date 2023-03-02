'''
N X N 크기의 단어 퍼즐에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램
'''

import sys
sys.stdin = open('1979_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    result = []
    # 1. 가로 검사
    for i in range(N):
        count = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                count += 1
            else:
                result.append(count)
                count = 0
        result.append(count)
    # 2. 세로 검사
    for j in range(N):
        count = 0
        for i in range(N):
            if puzzle[i][j] == 1:
                count += 1
            else:
                result.append(count)
                count = 0
        result.append(count)

    print(f'#{tc}', result.count(K))




