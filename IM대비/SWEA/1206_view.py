'''
왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다
빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오
'''
import sys
sys.stdin = open('1206_input.txt')

for tc in range(1, 11):
    N = int(input())
    tower_high = list(map(int, input().split()))

    # 조망권 초기값 설정
    view = 0
    # 맨 왼쪽 두 칸과 맨 오른쪽 두 칸은 건물 X 비교 대상 아님
    for i in range(2, N-2):
        dis1 = tower_high[i] - tower_high[i-2]
        dis2 = tower_high[i] - tower_high[i-1]
        dis3 = tower_high[i] - tower_high[i+1]
        dis4 = tower_high[i] - tower_high[i+2]
        # 양쪽 모두 거리 2이상의 공간이 확보될 때 조망권이 확보됨
        if dis1 > 0 and dis2 > 0 and dis3 > 0 and dis4 > 0:
            view += min(dis1, dis2, dis3, dis4)

    print(f'#{tc} {view}')

