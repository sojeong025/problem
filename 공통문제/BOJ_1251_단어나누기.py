import sys
sys.stdin = open('input.txt')

word = input()

for i in range(1, len(word)):
    for j in range(2, len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]

        re_a, re_b, re_c = a[::-1], b[::-1], c[::-1]
