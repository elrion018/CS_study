import sys


def bt(res, channel):
    global minVal
    if res != "" and len(res) == len(str(channel))-1:
        press_cnt = len(res)
        minVal = min(minVal, abs(int(res)-channel) + press_cnt)
    if len(res) == len(str(channel)):
        press_cnt = len(res)
        minVal = min(minVal, abs(int(res)-channel) + press_cnt)
    if len(res) == len(str(channel))+1:
        press_cnt = len(res)
        minVal = min(minVal, abs(int(res)-channel) + press_cnt)
        return

    for i in range(10):
        if table[i] == 1:
            res += str(i)
            bt(res, channel)
            res = res[:-1]


channel = int(sys.stdin.readline())
wrong_cnt = int(sys.stdin.readline())
wrong_btn = list(map(int, sys.stdin.readline().split()))
table = [1]*10

for i in wrong_btn:
    table[i] = 0

minVal = abs(channel-100)
res = ""
bt(res, channel)
print(minVal)
