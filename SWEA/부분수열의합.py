import sys
sys.stdin = open('input.txt')

def dsf(idx, now):
    global result

    if now > K:
        return
    
    if now == K:
        result += 1
        return
    
    if idx == N:
        if now == K:
            result += 1
        return
    
    dsf(idx + 1, now + arr[idx])
    dsf(idx + 1, now)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0

    dsf(0, 0)
    print(result)


