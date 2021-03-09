import sys

def four_way_spread(y,x, room, temp1, temp2):
		dy = [0,0,1,-1]
		dx = [1,-1,0,0]

		if room[y][x] > 0:
				for k in range(4):
						ay = y + dy[k]
						ax = x + dx[k]
						if ay >= 0 and ay <r and ax>=0 and ax <c and room[ay][ax] != -1:
								part = room[y][x] // 5
								temp1[ay][ax] += part
								temp2[y][x] += part
								
		return room, temp1, temp2

def sum_dust(r,c,room, temp1,temp2):
		for y in range(r):
				for x in range(c):
					room[y][x] += temp1[y][x]
					room[y][x] -= temp2[y][x]

		return room

def spread_dust(r,c,room):
		temp1 = [[0]*c for _ in range(r)]
		temp2 = [[0]*c for _ in range(r)]

		for y in range(r):
				for x in range(c):
						room, temp1, temp2 = four_way_spread(y,x, room, temp1, temp2)

		room = sum_dust(r,c, room, temp1, temp2)
		return room

def wind_dust(r,c, room):
		cleaner_y = None
		for y in range(r):
			for x in range(c):
				if room[y][x] == -1:
					cleaner_y = y
					break
		
		area1 = room[0:cleaner_y]
		area2 = room[cleaner_y:]
		
		# area 1 (반시계 방향)
		area1 = wind_area1(area1,c)
		area2 = wind_area2(area2,c)


		return area1 + area2
		# area 2 (시계 방향)

def wind_area1(area1,c):
		temp = [[0]*c for _ in range(len(area1))]
		for y in range(len(area1)):
			for x in range(c):
				if y-1 < 0 and x-1 < 0: #왼쪽 상단 구석
					temp[y+1][x] = area1[y][x]
				elif y-1 <0 and x +1 == c: #오른쪽 상단 구석
					temp[y][x-1] = area1[y][x]
				elif y+1 == len(area1) and x -1 <0: # 왼쪽 하단 구석
					temp[y][x+1] = area1[y][x]
				elif y+1 == len(area1) and x + 1 == c: # 오른쪽 하단 구석
					temp[y-1][x] = area1[y][x]
				elif y-1 <0:
						temp[y][x-1] = area1[y][x]
				elif y+1 == len(area1):
						temp[y][x+1] = area1[y][x]
				elif x-1 <0:
						temp[y+1][x] = area1[y][x]
				elif x+1 == c:
						temp[y-1][x] = area1[y][x]
				else:
						temp[y][x] = area1[y][x]

		area1 = overwrite_area(temp, area1, c)
		return area1

def wind_area2(area2,c):
		temp = [[0]*c for _ in range(len(area2))]
		for y in range(len(area2)):
			for x in range(c):
				if y-1 < 0 and x-1 < 0: #왼쪽 상단 구석
					temp[y][x+1] = area2[y][x]
				elif y-1 <0 and x +1 == c: #오른쪽 상단 구석
					temp[y+1][x] = area2[y][x]
				elif y+1 == len(area2) and x -1 <0: # 왼쪽 하단 구석
					temp[y-1][x] = area2[y][x]
				elif y+1 == len(area2) and x + 1 == c: # 오른쪽 하단 구석
					temp[y][x-1] = area2[y][x]
				elif y-1 <0:
						temp[y][x+1] = area2[y][x]
				elif y+1 == len(area2):
						temp[y][x-1] = area2[y][x]
				elif x-1 <0:
						temp[y-1][x] = area2[y][x]
				elif x+1 == c:
						temp[y+1][x] = area2[y][x]
				else:
						temp[y][x] = area2[y][x]
				
		area2 = overwrite_area(temp, area2, c)
		return area2

def overwrite_area(temp, area,c):
		for y in range(len(area)):
			for x in range(c):
					if area[y][x] != -1:
							if temp[y][x] == -1:
								area[y][x] = 0
							else:
								area[y][x] = temp[y][x]

		return area

def get_answer(r,c, room):
		answer = 0
		for y in range(r):
			for x in range(c):
				if room[y][x] != -1:
					answer += room[y][x]
		return answer

def solution(r,c,t, room):
		for _ in range(t):
			room = spread_dust(r,c,room)
			room = wind_dust(r,c, room)


		return get_answer(r,c,room)

r,c,t = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

print(solution(r,c,t, room))