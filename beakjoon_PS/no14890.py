

def judge(heights):
    current = heights[0]
    visited = [False for _ in range(N)]

    for i, height in enumerate(heights):

        if current == height:
            continue
        elif current + 1 == height:  # 높이 올라가는 경우
            for j in range(i-1, i-1-L, -1):
                if j < 0 or current != heights[j] or visited[j] == True:
                    return False
                else:
                    visited[j] = True
            current = height
        elif current - 1 == height:  # 낮게 내려가는 경우
            for j in range(i, i+L):

                if j >= N or current - 1 != heights[j] or visited[j] == True:
                    return False
                else:
                    visited[j] = True
            current = height
        else:
            return False

    return True


def solve():
    count = 0
    # 각 행과 열들 검증하고 카운팅
    # 행에 대하여
    for y in range(N):
        if judge(arr[y]):
            count += 1
        # 열에 대하여
    for x in range(N):
        path = []
        for y in range(N):
            path.append(arr[y][x])

        if judge(path):
            count += 1

    return print(count)


if __name__ == '__main__':
    N, L = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    solve()
