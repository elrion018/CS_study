T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    zero_people = [i for i in range(1,n+1)]
    for j in range(k):
        for l in range(n-1):
            zero_people[l+1]+=zero_people[l]
    print(zero_people[-1])



    


