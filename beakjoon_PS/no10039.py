score_list = []
for i in range(5):
    score = int(input())
    if 0<=score<=100 and score % 5 == 0:
        if score>=40:
            score_list.append(score)
        else:
            score = 40
            score_list.append(score)
score_mean = sum(score_list)/ len(score_list)
print('%.0f' % score_mean)