def backtracking(tmp, depth, c):
    global result

    if c > cal:
        return
    result = max(result, tmp)
    if depth == n:
        return

    backtracking(tmp + lst[depth][0], depth + 1, c + lst[depth][1])
    backtracking(tmp, depth+1, c)



T = int(input())
for tc in range(1, T+1):
    n, cal = map(int,input().split())

    lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))

    result = 0
    backtracking(0,0,0)
    print(f'#{tc}', result)
