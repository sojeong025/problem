'''
N개의 과목에 대한 시험 - 성적표에는 이 중에서 정확히 K개의 과목을 선택하여 넣을 수 있다
최대로 만들 수 있는 총점은 몇점인지
'''

import sys
sys.stdin = open('4466_input.txt')

T = int(input())
for tc in range(1, T+1):
    # N 개의 과목 / K 개 선택
    N, K = map(int, input().split())
    score = sorted(list(map(int, input().split())), reverse=True)

    print(f'#{tc} {sum(score[:K])}')




