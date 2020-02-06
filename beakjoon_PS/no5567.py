n = int(input())
m = int(input())
tfs = [list(map(int, input().split())) for _ in range(m)]
sfs = []
sffs = []
# 상근이의 친구 구하기
for sf in tfs:
    if 1 in sf:
        sfs.append(sf)
# 상근이의 친구의 친구 구하기
for sf in sfs:
    for sff in tfs:
        if sf[1] in sff:
            sffs.append(sff)

result = sum(sffs + sfs, [])
print(len(set(result))-1)
