word = list(input().upper())
word_two = list(set(word))
cnt = []
for j in range(len(word_two)):
    cnt.append(0)
for i in word:
    if i in word_two:
        cnt[word_two.index(i)] +=1
if cnt.count(max(cnt)) == 1:
    print(word_two[cnt.index(max(cnt))])
else:
    print('?')
    
