def binary_search(M, trees):
    trees.sort()
    start = 1
    end = max(trees)
    ans = 0
    while start <= end:
        mid = (start+end) // 2
        temp = 0
        for i in trees:
            if mid <= i:
                temp += i - mid
        if temp >= M:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return print(ans)


N, M = map(int, input().split())
trees = list(map(int, input().split()))
binary_search(M, trees)
