import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

col = p
row = q
count = 0

while True:
    col += 1
    row += 1
    if row == h:
        q -= 1
    elif row == 0:
        q += 1

    if col == w:
        p -= 1
    elif col == 0:
        p += 1

    count += 1
    if t == count:
        print((col, row))
        break
