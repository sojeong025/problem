import sys
sys.stdin = open('16811_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()

    size = [0] * 31
    for c in carrot:
        size[c] += 1

    minV = 1000
    for i in range(29):
        for j in range(30):
            A = sum(size[1:i+1])
            B = sum(size[i+1:j+1])
            C = sum(size[j+1:31])
            if A*B*C != 0 and A <= N//2 and B <= N//2 and C <= N//2:
                diff = max(A, B, C) - min(A, B, C)
                if minV > diff:
                    minV = diff
    if minV == 1000:
        minV = -1
    print(f'#{tc} {minV}')

    # minV = 1000
    # for i in range(N-2):  # 소 박스
    #     for j in range(i+1, N-1):  # 중 박스
    #         # 같은 크기가 다른 박스에 들어가는 경우 제외하고
    #         if carrot[i]!=carrot[i+1] and carrot[j]!=carrot[j+1]:
    #             A = i + 1
    #             B = j - i
    #             C = N - 1 - j
    #             if A*B*C!=0 and A <= N//2 and B <= N//2 and C <= N//2:
    #                 if minV > max(A, B, C) - min(A, B, C):
    #                     minV = max(A, B, C) - min(A, B, C)
    # if minV == 1000:
    #     minV = -1
    # print(f'#{tc} {minV}')


