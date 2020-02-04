result = 0
order = []
scores = [[int(input()), i+1] for i in range(8)]
scores = sorted(scores, reverse=True)
for j in range(5):
    order.append(scores[j][1])
    result += scores[j][0]
print(result)
for k in sorted(order):
    print(k, end=' ')
