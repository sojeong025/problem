"""
'<'와 '>' 가 k개 나열된 순서열 A : 부등호 사이 0부터 9까지의 숫자
제시된 K개 부등호 순서 만족하는 K+1 정수 중에서 최댓값과 최솟값 찾아야함

check 함수 : sign 부등호 종류로 i와 j 선택 -> 백트래킹 활용

"""


def check(i, j, k):
    if k == '<':
        return i < j
    else:
        return i > j


def backtracking(depth, tmp):
    global max_num, min_num

    if depth == K + 1:
        if len(min_num) == 0:
            min_num = tmp
        else:
            max_num = tmp
        return

    else:
        for l in range(10):
            if not visited[l]:
                if depth == 0 or check(tmp[-1], str(l), sign[depth-1]):
                    visited[l] = 1
                    backtracking(depth+1, tmp + )




import sys
sys.stdin = open('input.txt')

K = int(input())
sign = input().split()

visited = [0] * K

max_num = ""
min_num = ""
