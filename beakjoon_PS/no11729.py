import sys


def hanoi(num, f, to, other):
    global K
    if num == 0:
        return

    hanoi(num-1, f, other, to)
    arr.append([f, to])
    K += 1
    hanoi(num-1, other, to, f)


N = int(sys.stdin.readline())
arr = []
K = 0
hanoi(N, 1, 3, 2)
print(K)
for ele in arr:
    print(ele[0], ele[1])
