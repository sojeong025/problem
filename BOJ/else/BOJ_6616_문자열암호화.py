import sys
sys.stdin = open('input.txt')

while True:
    N = int(input())
    if N == 0:
        break
    text = "".join(input().split()).upper()

