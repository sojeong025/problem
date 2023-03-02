'''
푸른 자성체의 경우 N극에 이끌리는 성질을 가지고 있고, 붉은 자성체의 경우 S극에 이끌리는 성질
일정 간격을 두고 강한 자기장을 걸었을 때, 시간이 흐른 뒤에 자성체들이 서로 충돌하여 테이블 위에 남아있는 교착 상태의 개수
'''

import sys
sys.stdin = open('1220_input.txt')

for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]

    # 1이 N극 2가 S극
    answer = 0
    for i in range(N):
        temp = 0
        for j in range(N):
            # 만약 1이면 교착 상태가 될 수 있으니 상태 확인할 변수 temp에 1
            if table[j][i] == 1:
                temp = 1
            # 값이 2일 때, 상태가 1이면 교착상태 -> 답에 +1 해준 뒤 temp 0으로 리셋
            elif table[j][i] == 2:
                if temp == 1:
                    answer += 1
                    temp = 0
    print(f'#{tc} {answer}')

