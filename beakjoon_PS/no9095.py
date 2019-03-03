T = int(input())
result = []
for _ in range(T):
    lst = [1,2,3]
    num = int(input())
    while lst.count(num) != len(lst):
        temp = []
        for i in lst:
            if i != num:
                if i+1 <num+1:
                    temp.append(i+1)
                if i+2 <num+1:
                    temp.append(i+2)
                if i+3 <num+1:
                    temp.append(i+3)
            else:
                temp.append(i)
            lst = []
            lst = temp
    print(len(lst))
        
            
