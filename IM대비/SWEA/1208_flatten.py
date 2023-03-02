'''
높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업
평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다
평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때,
제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램
'''

import sys
sys.stdin = open('1208_input.txt')

for tc in range(1, 11):
    dump = int(input())  # 덤프 횟수
    box = list(map(int, input().split()))

    for i in range(dump):
        max_box = max(box)
        min_box = min(box)
        max_idx = box.index(max_box)
        min_idx = box.index(min_box)

        # 최고점의 인덱스에 있는 박스는 -1씩, 최저점의 인덱스에 있는 박스는 +1씩
        box[max_idx] -= 1
        box[min_idx] += 1

    # dump 의 횟수만큼 반복문을 마친 뒤, 최고점과 최저점의 차이 반환
    answer = max(box) - min(box)
    print(f'#{tc} {answer}')

