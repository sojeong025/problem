'''
N x N 행렬이 주어질 때,
시계 방향으로 90도, 180도, 270도 회전한 모양을 출력
'''

import sys
sys.stdin = open('1961_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    arr2 = list(map(list, zip(*arr)))

    print(f'#{tc}')
    for i in range(N):
        print(f'{"".join(arr2[i][::-1])} {"".join(arr[N-1-i][::-1])} {"".join(arr2[N-1-i])}')
