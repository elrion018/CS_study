import sys


def bt(count, idx):
    global maxVal
    if K < 5:
        return
    if count == K-5 or count == len(alpha):
        word_cnt = 0
        for word in words:
            word = list(word)
            judge1 = True
            for i in word:
                if table[ord(i)-97] == False:
                    judge1 = False
                    break
            if judge1 == True:
                word_cnt += 1

        if maxVal < word_cnt:
            maxVal = word_cnt
        return
    for i in range(idx, len(alpha)):
        if table[ord(alpha[i])-97] == False:
            table[ord(alpha[i])-97] = True
            bt(count+1, i)
            table[ord(alpha[i])-97] = False


N, K = map(int, sys.stdin.readline().split())
alpha = []
words = []
for _ in range(N):
    word = sys.stdin.readline().strip()
    words.append(word)
    temp = list(word)[4:-4]
    alpha = alpha+temp
alpha = list(set(alpha))

antic = ['a', 'n', 't', 'i', 'c']
table = [False] * 26
for i in antic:
    table[ord(i)-97] = True
temp = []
for j in alpha:
    if j not in antic:
        temp.append(j)
alpha = temp
maxVal = 0
count = 0
bt(count, 0)
print(maxVal)
