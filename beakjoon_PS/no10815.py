import sys
sys.setrecursionlimit(10**6)


def binary_search(cards, key, left, right):

    if left > right:
        return print(0, end=' ')

    mid = (left + right) // 2

    if cards[mid] == key:

        return print(1, end=' ')

    elif cards[mid] > key:
        binary_search(cards, key, left, mid-1)
    else:
        binary_search(cards, key, mid + 1, right)


N = int(input())

cards = list(map(int, input().split()))

cards.sort()

M = int(input())

for key in list(map(int, input().split())):
    binary_search(cards, key, 0, N-1)
