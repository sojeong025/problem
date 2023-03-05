# 상근 설탕배달 - N킬로그램  - 3키로 봉지와 5키로 봉지 있음
# 최대한 적은 봉지

import sys
sys.stdin = open('input.txt')

N = int(input())

sugar = 0
while N >= 0:
    if N % 5 == 0:
        sugar += (N//5)
        print(sugar)
        break
    N -= 3
    sugar += 1
else:
    print(-1)