'''
다음 100X100의 2차원 배열이 주어질 때,
각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램
'''

import sys
sys.stdin = open('1209_input.txt')

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    # 행 우선 조회
    for i in range(100):
        sum = 0
        for j in range(100):
           sum += arr[i][j]
           if sum > max_sum:
               max_sum = sum
    # 열 우선 조회
    for j in range(100):
        sum = 0
        for i in range(100):
            sum += arr[i][j]
            if sum > max_sum:
                max_sum = sum
    # 대각선 조회
    sum1, sum2 = 0, 0
    for i in range(100):
        sum1 += arr[i][i]
        sum2 += arr[i][99-i]
        if max(sum1, sum2) > max_sum:
            max_sum = max(sum1, sum2)

    print(f'#{tc} {max_sum}')

