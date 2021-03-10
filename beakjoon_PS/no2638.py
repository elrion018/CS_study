import sys, collections

def search_air(cheese,n,m):
	air = [[0] * m for _ in range(n)]

	count = 2

	for y in range(n):
		for x in range(m):
			if cheese[y][x] == 0 and air[y][x] == 0:
					air = bfs_air(y,x,n,m, count,cheese, air)
					count += 1

	return air

def bfs_air(y,x, n, m, count, cheese, air):
		q = collections.deque()
		q.append([y,x])
		air[y][x] = count

		dy = [0,0,1,-1]
		dx = [1,-1,0,0]

		while q:
			by, bx = q.popleft()

			for i in range(4):
				ay = by + dy[i]
				ax = bx + dx[i]

				if ay >= 0 and ay < n and ax>= 0 and ax <m and cheese[ay][ax] == 0 and air[ay][ax] == 0:
					air[ay][ax] = count
					q.append([ay,ax])

		return air


def melt_cheese(cheese, air, n,m):
	melted_cheese = [[0] * m for _ in range(n)]

	dy = [0,0, 1, -1]
	dx = [1,-1, 0, 0]

	for y in range(n):
		for x in range(m):
			if cheese[y][x] == 1:
				count = 0
				for i in range(4):
					ay = y + dy[i]
					ax = x + dx[i]
					if air[ay][ax] == 2:
						count += 1
				
				if count < 2:
					melted_cheese[y][x] = 1

	return melted_cheese

def search_cheese(cheese,n,m):

		for y in range(n):
			for x in range(m):
				if cheese[y][x] == 1:
					return True

		return False


def solution(cheese, n, m):
		time = 0

		while True:
			air = search_air(cheese,n,m)
			cheese = melt_cheese(cheese, air, n,m)

			time += 1

			if search_cheese(cheese, n,m) == False:
				return time

n, m = map(int, sys.stdin.readline().split())

cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(solution(cheese, n,m))
