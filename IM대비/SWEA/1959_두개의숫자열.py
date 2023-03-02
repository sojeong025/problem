'''
N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M)
Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다
서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값
'''

import sys
sys.stdin = open('1959_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 만약 N이 M보다 크다면 자리 바꿔주기
    if N > M:
        N, M = M, N
        A, B = B, A

    max_sum = 0
    # 더 긴 쪽의 양 끝을 벗어나면 안되니 M-N+1로 범위 설정
    for i in range(M-N+1):
        temp = 0
        # 작은 범위의 인덱스로 돌아야 함
        for j in range(N):
            temp += A[j] * B[j+i]

        if temp > max_sum:
            max_sum = temp

    print(f'#{tc} {max_sum}')
