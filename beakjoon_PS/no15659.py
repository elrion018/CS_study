import sys
import collections


def backTracking(plus, minus, times, divide, idx, count, nums, op):
    print(count)
    # *, / 있으면 우선 연산
    if len(op) != 0 and len(nums) != 0 and (op[-1] == '*' or op[-1] == '/'):
        operator = op.pop()
        if operator == '*':
            temp = nums.pop() * seq[idx]
        elif operator == '/':
            temp = nums.pop() // seq[idx]
        if plus:
            nums.append(temp)
            op.append('+')
            backTracking(plus-1, minus, times, divide,
                         idx+1, count+1, nums, op)
            nums.pop()
            op.pop()
        if minus:
            nums.append(temp)
            op.append('-')
            backTracking(plus, minus-1, times, divide,
                         idx+1, count+1, nums, op)
            nums.pop()
            op.pop()
        if times:
            nums.append(temp)
            op.append('*')
            backTracking(plus, minus, times-1, divide,
                         idx+1, count+1, nums, op)
            nums.pop()
            op.pop()

        if divide:
            nums.append(temp)
            op.append('/')
            backTracking(plus, minus, times, divide-1,
                         idx+1, count+1, nums, op)
            nums.pop()
            op.pop()
    if count == N-1:
        nums.append(temp)
        # if operator == '*':
        #     times -= 1
        # elif operator == '/':
        #     divide -= 1
        print(nums, "final nums")
        return
    else:
        if plus:
            nums.append(seq[idx])
            op.append('+')
            backTracking(plus-1, minus, times, divide,
                         idx+1, count+1, nums, op)
            nums.pop()
            op.pop()
        if minus:
            nums.append(seq[idx])
            op.append('-')
            backTracking(plus, minus-1, times, divide,
                         idx+1, count+1, nums, op)
            nums.pop()
            op.pop()
        if times:
            nums.append(seq[idx])
            op.append('*')
            print(op)
            backTracking(plus, minus, times-1, divide,
                         idx+1, count+1, nums, op)
            print(op)
            nums.pop()
            op.pop()

        if divide:
            nums.append(seq[idx])
            op.append('/')
            backTracking(plus, minus, times, divide-1,
                         idx+1, count+1, nums, op)
            nums.pop()
            op.pop()


N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
plus, minus, times, divide = map(int, sys.stdin.readline().split())
backTracking(plus, minus, times, divide, 0, 0,
             collections.deque(), collections.deque())
