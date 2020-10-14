import sys
import collections


def bfs(caseList):
    result = 1
    queue = collections.deque()
    queue.append((caseList[0]//5, caseList[0] % 5))
    visited = [[False]*5 for _ in range(5)]
    visited[caseList[0]//5][caseList[0] % 5] = True
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ay = y + dy[i]
            ax = x + dx[i]
            if ay >= 0 and ay < 5 and ax >= 0 and ax < 5:
                if visited[ay][ax] == False and (5*ay + ax) in caseList:
                    visited[ay][ax] = True
                    result += 1
                    queue.append((ay, ax))

    return result


def bt(count, S, caseList):
    global cases
    if count == 7 and S >= 4:
        if bfs(caseList) == 7:
            cases += 1
            return
        return
    if len(caseList) != 0:
        for y in range(caseList[-1] // 5, 5):
            if y == (caseList[-1] // 5):
                for x in range(caseList[-1] % 5, 5):
                    if caseList[-1] < (5*y+x):
                        caseList.append(5*y + x)
                        if arr1[y][x] == 'S':
                            bt(count+1, S+1, caseList)
                        else:
                            bt(count+1, S, caseList)
                        caseList.pop()
            else:
                for x in range(5):
                    if caseList[-1] < (5*y+x):
                        caseList.append(5*y + x)
                        if arr1[y][x] == 'S':
                            bt(count+1, S+1, caseList)
                        else:
                            bt(count+1, S, caseList)
                        caseList.pop()

    else:
        for y in range(5):
            for x in range(5):
                caseList.append(5*y + x)
                if arr1[y][x] == 'S':
                    bt(count+1, S+1, caseList)
                else:
                    bt(count+1, S, caseList)
                caseList.pop()


arr1 = [list(sys.stdin.readline().strip()) for _ in range(5)]

cases = 0

bt(0, 0, [])
print(cases)
