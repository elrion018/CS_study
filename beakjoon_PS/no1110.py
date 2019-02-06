first_num = int(input())
check_num = first_num
sum_num = 0
new_num = 0
cnt = 0
while True:
    if first_num < 10:
        first_num = 10*first_num
        sum_num = (first_num // 10) + (first_num % 10)
        new_num = 10*(first_num % 10) + (sum_num % 10)
        first_num = new_num
        cnt += 1
        if first_num == check_num:
            print(cnt)
            break        
    else:
        sum_num = (first_num // 10) + (first_num % 10)
        new_num = 10*(first_num % 10) + (sum_num % 10)
        first_num = new_num
        if first_num == check_num:
            print(cnt)
            break


