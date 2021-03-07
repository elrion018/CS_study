import sys

t=  int(sys.stdin.readline())


for _ in range(t):
	l, n = map(int,sys.stdin.readline().split())
	points = []
	minCondition = sys.maxsize
	maxCondition = sys.maxsize
	minVal = None
	maxVal = None

	for _ in range(n):
		points.append(int(sys.stdin.readline()))

	for i in range(len(points)):
		if abs(l/2- points[i]) < minCondition and points[i] < l/2:
			minCondition = abs(l/2- points[i])
			minVal = points[i]
		if abs(l/2- points[i]) < minCondition and points[i] >= l/2:
			minCondition = abs(l/2- points[i])
			minVal = abs(l-points[i])
		if abs(l-points[i]) < maxCondition and points[i] >= l/2:
			maxCondition = abs(l-points[i])
			maxVal = points[i]
		if points[i] < maxCondition and points[i] < l/2:
			maxCondition = points[i]
			maxVal = l - points[i]
				
		
	
	print(minVal, maxVal)
	
