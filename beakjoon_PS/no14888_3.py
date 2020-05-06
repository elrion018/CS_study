import sys


def backTracking(calVal, idx, count, plus, minus, times, divide):
    global minVal, maxVal, seq, N
    if count == N-1:
        if minVal > calVal:
            minVal = calVal
        if maxVal < calVal:
            maxVal = calVal
        return
    else:
        if plus:
            backTracking(calVal + seq[idx], idx+1,
                         count+1, plus-1, minus, times, divide)
        if minus:
            backTracking(calVal -
                         seq[idx], idx+1, count+1, plus, minus-1, times, divide)
        if times:
            backTracking(calVal * seq[idx], idx+1,
                         count+1, plus, minus, times-1, divide)

        if divide:
            if calVal > 0:
                backTracking(calVal // seq[idx], idx+1,
                             count+1, plus, minus, times, divide-1)
            else:
                backTracking(-(abs(calVal) // seq[idx]), idx+1,
                             count+1, plus, minus, times, divide-1)


N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
minVal = sys.maxsize
maxVal = -sys.maxsize
calVal = seq[0]
count = 0
idx = 1
plus, minus, times, divide = map(int, sys.stdin.readline().split())
backTracking(calVal, idx, count, plus, minus, times, divide)
print(maxVal)
print(minVal)
