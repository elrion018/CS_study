import sys

n = int(sys.stdin.readline())

room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[[0,0,0] for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1


for y in range(n):
	for x in range(n):
		for z in range(3):
			if z ==0:
				if x+1 < n and room[y][x+1] != 1:
					dp[y][x+1][0] += dp[y][x][0]
				if x+1 < n and y+1 < n and room[y+1][x+1] !=1 and room[y][x+1] != 1 and room[y+1][x] != 1:
					dp[y+1][x+1][1] += dp[y][x][0]
			if z == 1:
				if x+1 < n and room[y][x+1] != 1:
					dp[y][x+1][0] += dp[y][x][1]
				if x+1 < n and y+1 < n and  room[y+1][x+1] !=1 and room[y][x+1] != 1 and room[y+1][x] != 1:
					dp[y+1][x+1][1] += dp[y][x][1]
				if y+1 < n and room[y+1][x] != 1:
					dp[y+1][x][2] += dp[y][x][1]
			if z == 2:
				if y+1 < n and room[y+1][x] != 1:
					dp[y+1][x][2] += dp[y][x][2]
				if x+1 < n and y+1 < n and  room[y+1][x+1] !=1 and room[y][x+1] != 1 and room[y+1][x] != 1:
					dp[y+1][x+1][1] += dp[y][x][2]

print(sum(dp[n-1][n-1]))
