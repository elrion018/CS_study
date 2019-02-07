n = list(input().split(' '))
while '' in n:
    n.remove('')
if len(n) < 1000000:

    print(len(n))