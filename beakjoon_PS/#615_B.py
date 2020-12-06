import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    p = []
    for _ in range(n):
        x, y = list(map(int, sys.stdin.readline().split()))
        sumVal = x+y
        p.append([x, y, sumVal])
    p = sorted(p, key=lambda ele: ele[2])
    string = ""
    now = [0, 0]
    judge1 = True
    for ele in p:
        x_dist = ele[0] - now[0]
        y_dist = ele[1] - now[1]
        if x_dist < 0 or y_dist < 0:
            judge1 = False
            break
        else:
            if x_dist != 0:
                for _ in range(x_dist):
                    string += "R"
            if y_dist != 0:
                for _ in range(y_dist):
                    string += "U"
        now = [ele[0], ele[1]]
    if judge1 == True:
        print("YES")
        print(string)
    else:
        print("NO")
