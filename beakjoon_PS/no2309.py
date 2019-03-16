target_num = 100

#전체 합 구하기
Sum = 0
data = []
for _ in range(9):
    temp = int(input())
    data.append(temp)
    Sum += temp

#오름차순 정렬
data = sorted(data)
data2 = data
# #2개를 빼서 비교
for i in range(9):
    for j in range(9):
        if data[i] == data[j]:
            continue
        temp = data[i] + data[j]
        if Sum - temp == target_num:
            for k in data2:
                if k != data[i] and k != data[j]:
                    print(k)