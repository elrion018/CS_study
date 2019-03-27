count = 0
for i in range(10):
    T = int(input())
    BL = list(map(int,input().split()))
    # print(BL)
    result = 0
    count += 1
#각 건물의 경우 따지기
    for j in range(len(BL)):
        left = None
        right = None
        # print(BL[j])

        if BL[j] == 0: #건물 층수가 0이라면 넘기기
            continue
#왼쪽전망
        if BL[j]>BL[j-2] and BL[j]>BL[j-1]:
            if BL[j-2] > BL[j-1]:
                left = BL[j] - BL[j-2]
                
            else:
                left = BL[j] - BL[j-1]
#오른쪽 전망
            if BL[j]>BL[j+2] and BL[j]>BL[j+1]:
                if BL[j+2] > BL[j+1]:
                    right = BL[j] - BL[j+2]
                else:
                    right = BL[j] - BL[j+1]
#왼쪽 오른쪽 다 만족하는 층 구하기
            if left is not None and right is not None: 
                if left > right:
                    result += right
                else:
                    
                    result += left
    print("#%s %d" % (count, result))