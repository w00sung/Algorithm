
import sys
read = sys.stdin.readline

n = int(read())
word = []
word_li = []
for _ in range(n):
    word.append(read().rstrip())
# 고유값
word = list(set(word))

for w in word:
    word_li.append((w,len(w)))

word_li.sort(key = lambda x : (x[1],x[0]))

# 길이 같은 것 끼리 묶기
print(word_li)

for i in range(len(word_li)):
    print(word_li[i][0])