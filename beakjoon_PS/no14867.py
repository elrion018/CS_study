import sys
import collections


def bfs(a, b, c, d):
    visited = dict()
    queue = collections.deque()
    queue.append((0, 0))
    visited[(0, 0)] = 0

    while queue:
        y, x = queue.popleft()
        if (c, d) in visited and y == c and x == d:
            return print(visited[(c, d)])

        # fill(A)
        if y < a and not (a, x) in visited:
            visited[(a, x)] = visited[(y, x)] + 1
            queue.append((a, x))

        # fiil(B)
        if x < b and not (y, b) in visited:
            visited[(y, b)] = visited[(y, x)] + 1
            queue.append((y, b))

        if not (0, x) in visited:   # empty(A)
            visited[(0, x)] = visited[(y, x)] + 1
            queue.append((0, x))

        if not (y, 0) in visited:  # empty(B)
            visited[(y, 0)] = visited[(y, x)] + 1
            queue.append((y, 0))

        # move(A,B)
        if not (0, x+y) in visited and y <= b-x:
            visited[(0, x+y)] = visited[(y, x)] + 1
            queue.append((0, x+y))

        if not (y-(b-x), b) in visited and y > b-x:
            visited[(y-(b-x), b)] = visited[(y, x)] + 1
            queue.append((y-(b-x), b))

        # move(B,A)
        if not (y+x, 0) in visited and x <= a-y:
            visited[(y+x, 0)] = visited[(y, x)] + 1
            queue.append((y+x, 0))

        if not (a, x-(a-y)) in visited and x > a-y:
            visited[(a, x-(a-y))] = visited[(y, x)] + 1
            queue.append((a, x-(a-y)))
    return print(-1)


a, b, c, d = map(int, sys.stdin.readline().split())
bfs(a, b, c, d)
