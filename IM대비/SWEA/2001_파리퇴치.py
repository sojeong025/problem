'''
M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 구하라
'''

import sys
sys.stdin = open('2001_input.txt')

T = int(input())
for tc in range(1, T+1):
    # NxN 행렬 MxM 파리채
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_die = 0
    for i in range(N-M+1):  # 파리채가 행렬을 넘어가면 안되므로
        for j in range(N-M+1):
            die = 0
            for k in range(M):  # 파리채 크기만큼의 갯수 합
                for l in range(M):
                    die += arr[k+i][l+j]  # 인덱스 설정 잘하기
            if die > max_die:   # 최대값 설정
                max_die = die

    print(f'#{tc} {max_die}')
