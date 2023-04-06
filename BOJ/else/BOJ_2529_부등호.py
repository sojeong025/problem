"""
조건 확인
부등호를 기준으로 한 인접 숫자들은 부등호가 성립되어야 함
(K+1)개 선택된 숫자가 모두 다르며, 최솟값 최대값 추출

"""

import sys
sys.stdin = open('input.txt')


def check(i, j, k):
    if k == '<':
        return i < j
    else:
        return i > j


def backtracking(depth, tmp):
    global max_num, min_num

    if depth == K + 1:
        # 맨 처음 생성된 tmp -> 최소값
        if len(min_num) == 0:
            min_num = tmp
        # 계속 대입 후 마지막에 생성된 tmp -> 최대값
        else:
            max_num = tmp
        return

    # 왼쪽 숫자 -> 현재 담겨진 숫자 중 가장 마지막 숫자 꺼내야 하므로 tmp[-1]
    # 오른쪽 숫자 -> 현재 tmp에 들어가려는 숫자 l -> check 함수 위해 str로 타입 변경
    else:
        for l in range(10):
            if not visited[l]:
                # 문자열이 아직 존재하지 않거나, 계산이 가능한 경우
                if depth == 0 or check(tmp[-1], str(l), sign[depth-1]):
                    visited[l] = 1
                    backtracking(depth+1, tmp + str(l))
                    visited[l] = 0

# K = 부등호 문자의 개수 -> 문자는 K+1개
K = int(input())
# 부등호 종류
sign = input().split()

visited = [0] * 10

max_num = ""
min_num = ""

backtracking(0, "")
print(max_num)
print(min_num)