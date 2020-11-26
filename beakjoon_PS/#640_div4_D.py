import sys
import collections

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = collections.deque(map(int, sys.stdin.readline().split()))
    move_cnt = 0
    judge = False
    total_a = 0
    total_b = 0
    a = 0
    b = 0
    while True:
        # alice
        temp_a = 0
        for i in range(len(arr)):
            a += arr[i]
            temp_a += arr[i]
            if i == len(arr) - 1 and a <= b:
                judge = True
            if a > b:
                for _ in range(i+1):
                    arr.popleft()
                break
        b = 0
        total_a += temp_a
        move_cnt += 1
        if judge == True or len(arr) == 0:
            print(move_cnt, total_a, total_b)
            break

        # bob
        temp_b = 0
        for j in range(len(arr)-1, -1, -1):
            b += arr[j]
            temp_b += arr[j]
            if j == 0 and b <= a:
                judge = True

            if b > a:
                for _ in range(len(arr)-j):
                    arr.pop()
                break
        a = 0
        total_b += temp_b
        move_cnt += 1
        if judge == True or len(arr) == 0:
            print(move_cnt, total_a, total_b)
            break
