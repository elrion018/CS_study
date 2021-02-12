import sys

dic = dict()
arr = []

N = int(sys.stdin.readline())

for _ in range(N):
    temp = sys.stdin.readline().strip()
    arr.append(temp)
    for i in range(len(temp)):
        if temp[i] not in dic:
            dic[temp[i]] = (10**(len(temp)-1-i))
        else:
            dic[temp[i]] += (10**(len(temp)-1-i))
dic = list(dic.items())
dic = sorted(dic, key=lambda ele: -ele[1])
dic = list(map(list, dic))
cnt = 9
for i in range(len(dic)):
    dic[i][1] = cnt
    cnt -= 1
temp = dict()

for i in range(len(dic)):
    temp[dic[i][0]] = dic[i][1]
dic = temp

res = 0

for voca in arr:
    for i in range(len(voca)):
        res += dic[voca[i]] * 10 ** (len(voca)-1-i)
print(res)
