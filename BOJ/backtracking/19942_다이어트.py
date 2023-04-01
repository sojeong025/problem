import sys
sys.stdin = open('input.txt')

"""
영양분의 각각 합이 최소 100, 70, 90, 10 이 되도록 + 비용이 최소
첫번째 줄에 최소 비용 출력
두번째 줄에 조건 만족하는 최소 비용 식재료의 번호를 오름차순으로 한줄로 출력
같은 비용의 집합이 하나 이상이면 사전 순으로 빠른 것을 출력
"""


def backtracking(i, tmp):
    global min_cost, cost

    sum_cost = sum(food[j][4] for j in i)




N = int(input())
mp, mf, ms, mv = list(map(int, input().split()))
food = [list(map(int, input().split())) for _ in range(N)]

min_cost = 500 * N
cost = []

