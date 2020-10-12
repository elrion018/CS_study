import sys


def bt(N, count, arr2):
    global ans1, ans2
    if N == count:
        result = None
        for ele in arr1:
            if ele[0] < 0 and ele[1] < 0:
                temp = (not arr2[abs(ele[0])-1]) or (not arr2[abs(ele[1])-1])
            elif ele[0] < 0:
                temp = (not arr2[abs(ele[0])-1]) or arr2[ele[1]-1]
            elif ele[1] < 0:
                temp = arr2[ele[0]-1] or (not arr2[abs(ele[1])-1])

            else:
                temp = arr2[ele[0]-1] or arr2[ele[1]-1]
            if result != None:
                result = result and temp
            else:
                result = temp
        if result == True:
            ans1 = 1
            temp2 = []
            for i in arr2:
                if i == False:
                    temp2.append("0")
                else:
                    temp2.append("1")
            ans2 = temp2
            return
        return

    arr2.append(True)
    bt(N, count + 1, arr2)
    arr2.pop()
    arr2.append(False)
    bt(N, count + 1, arr2)
    arr2.pop()


N, M = map(int, sys.stdin.readline().split())

ans1 = 0
ans2 = None

# 절 담는 어레이
arr1 = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
bt(N, 0, [])

if ans1 == 1:
    print(ans1)
    print(" ".join(ans2))
else:
    print(0)
