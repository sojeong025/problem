import sys
sys.stdin = open('input.txt')

N = int(input())
team = [list(map(int, input().split())) for _ in range(N)]
answer = []


def divide(s, l):
    sum_start = 0
    for i in s:
        for j in s:
            if i == j :
                continue
            sum_start += team[i][j]
    sum_link = 0
    for i in l:
        for j in l:
            if i == j:
                continue
            sum_link += team[i][j]
    answer.append(abs(sum_start - sum_link))

def DFS():
    if len(arr)






