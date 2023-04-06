import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     binary = input()
#     ternary = input()

#     # 2진수로 만들 수 있는 경우의 수
#     guess = []
#     for i in range(len(binary)):
#         # 해당 자리가 0이면 1로 바꾸고 10진수 변환해서 리스트에 넣기
#         if binary[i] == '0':
#             change = binary[:i] + '1' + binary[i+1:]
#             guess.append(int(change, 2))
#         # 해당 자리가 1이면 0으로 바꾸고 10진수 변환해서 리스트에 넣기
#         else:
#             change = binary[:i] + '0' + binary[i+1:]
#             guess.append(int(change, 2))
    
#     # 3진수로 사용할 숫자
#     ter = '012'
#     for i in range(len(ternary)):
#         for j in ter:
#             # 원래 숫자이면 넘어가기
#             if ternary[i] == j:
#                 continue
#             # 해당 자리(i) 숫자 바꿔서 10진수로 변환
#             change = int(ternary[:i] + j + ternary[i+1:], 3)
#             if change in guess:
#                 print(f'#{tc} {change}')
#                 break

T = int(input())
for tc in range(1,T+1):
    bin = list(input())
    tri = list(input())
    try_bin, try_tri = set(), set()
    for i in range(len(bin)):
        temp = bin[:]
        temp[i] = '0' if temp[i] == '1' else '1'
        try_bin.add(int(''.join(temp),2))
    for i in range(len(tri)):
        for j in range(3):
            temp = tri[:]
            if str(j) != temp[i]:
                temp[i] = str(j)
                try_tri.add(int(''.join(temp),3))
    print(f'#{tc}', *try_bin & try_tri)