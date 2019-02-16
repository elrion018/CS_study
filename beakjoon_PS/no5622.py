dial =input()
dial2 = list((' '.join(dial).split(' ')))
time = 0
if 2<= len(dial2) <= 15 and dial.isupper()==True:
    for i in dial2:
        if i in ['A','B','C']:
            time += 3
        elif i in ['D','E','F']:
            time += 4
        elif i in ['G','H','I']:
            time += 5
        elif i in ['J','K','L']:
            time += 6
        elif i in ['M','N','O']:
            time += 7
        elif i in ['P','Q','R','S']:
            time += 8
        elif i in ['T','U','V']:
            time += 9
        elif i in ['W','X','Y','Z']:
            time += 10
print(time)

