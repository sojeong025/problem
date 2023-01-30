# 최소, 최대

# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

N= int(input())
numbers=list(map(int, input().split()))

print(min(numbers), max(numbers))

# 반복문 활용
n= int(input())
nums=list(map(int,input().split()))
max_num = nums[0]
min_num = nums[0]
for i in nums:
    if i > max_num:
        max_num=i
    elif i < min_num:
        min_num=i
print(min_num, max_num)