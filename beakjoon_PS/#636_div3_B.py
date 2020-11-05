import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    if (n/2) % 2 == 1:
        print("NO")
        continue
    else:
        print("YES")
        arr1 = []
        even = 2
        for i in range(int((n/2))):
            arr1.append(even)
            if i % 2 == 0:
                even += 2
            else:
                even += 4
        arr2 = []
        odd = 1
        for j in range(int((n/2))):
            arr2.append(odd)
            if j % 2 == 0:
                odd += 4
            else:
                odd += 2
        for k in range(len(arr1)):
            print(arr1[k], end=" ")
        for l in range(len(arr2)):
            if l == len(arr2)-1:
                print(arr2[l])
            else:
                print(arr2[l], end=" ")
