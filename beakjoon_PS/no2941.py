word = list(' '.join(input()).split())
num = len(word)
for i in range(len(word)-1):
    for j in range(i+1,i+2):
        if word[i] + word[j] =='c=':
            num-= 1
        elif word[i] + word[j] =='c-':
            num-= 1
        elif word[i] + word[j] =='d-':
            num-= 1
        elif word[i] + word[j] =='lj':
            num-= 1
        elif word[i] + word[j] =='nj':
            num-= 1
        elif word[i] + word[j] =='s=':
            num-= 1
        elif word[i] + word[j] =='z=':
            num-= 1
for k in range(len(word)-2):
    if word[k] + word[k+1] +word[k+2] =='dz=':
        if word[k+1] + word[k+2] == 'z=':
            num-=1
        else:
            num-=2
print(num)