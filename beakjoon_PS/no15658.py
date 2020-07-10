import sys


def backTracking(plus, minus, times, divide, idx, result, count):
    global minVal, maxVal, N
    if count == N-1:
        if minVal > result:
            minVal = result

        if maxVal < result:
            maxVal = result

        return
    if plus:
        backTracking(plus-1, minus, times, divide, idx +
                     1, result + nums[idx], count + 1)
    if minus:
        backTracking(plus, minus-1, times, divide, idx +
                     1, result - nums[idx], count + 1)
    if times:
        backTracking(plus, minus, times-1, divide, idx +
                     1, result * nums[idx], count + 1)
    if divide:
        if result >= 0:
            backTracking(plus, minus, times, divide-1,
                         idx + 1, result // nums[idx], count + 1)
        elif result < 0:
            backTracking(plus, minus, times, divide-1, idx + 1, -
                         (abs(result) // nums[idx]), count + 1)


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
plus, minus, times, divide = map(int, sys.stdin.readline().split())
minVal = sys.maxsize
maxVal = -sys.maxsize
backTracking(plus, minus, times, divide, 1, nums[0], 0)
print(maxVal)
print(minVal)
