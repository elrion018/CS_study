import sys


def get_gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        n = a % b
        a = b
        b = n
    return a


T = int(sys.stdin.readline())

for _ in range(T):
    gcds = []
    temp = list(map(int, sys.stdin.readline().split()))
    n, nums = temp[0], temp[1:]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            gcds.append(get_gcd(nums[i], nums[j]))
    print(sum(gcds))
