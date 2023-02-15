word = input()

# 단어의 조합들을 담을 리스트
lst = []

for i in range(len(word)):
    # 뒤집은 단어들 조각 담을 곳
    rev = []
    for j in word:
        rev.append(word[0:i:] + word[i:]
