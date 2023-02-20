import sys
sys.stdin = open('input.txt')
word = input()

stack = []
result = 'yes'

for char in word:
    if char == '.':
        break
