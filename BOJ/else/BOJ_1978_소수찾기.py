n = int(input())
numbers = map(int, input().split())
res = 0
for num in numbers:
    cnt = 0
    if num ==1:
        continue
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                cnt += 1
        if cnt == 0:
            res += 1
print(res)