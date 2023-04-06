import sys
sys.stdin = open('input.txt')

# 10이 넘는 숫자를 위한 변환기
converter = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}



# T = int(input())
# for tc in range(1, T+1):
#     N, number = input().split()

#     result = ''

#     for n in number[::-1]:
#         if n in converter:
#             n = converter[n]

#         n = int(n)

#         for _ in range(4):
#             result = str(n%2) + result
#             n //= 2
#     print(f'#{tc} {result}')


T = int(input())
for tc in range(1, T+1):
    N, number = input().split()
    print(f'#{tc} ', end='')
    for n in range(len(number)):
        result = bin(int(number[n], base=16))[2:].zfill(4)
        print(result, end='')
    print()