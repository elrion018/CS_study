import sys

maxVal = 0

s1 = [0] + list(sys.stdin.readline().strip())
s2 = [0] + list(sys.stdin.readline().strip())

dp = [[[0,''] for _ in range(len(s1))] for _ in range(len(s2))]

answer = ''
for i in range(1, len(s2)):
		for j in range(1, len(s1)):
				if s2[i] == s1[j]:
						dp[i][j][0] = dp[i-1][j-1][0] +1
						dp[i][j][1] = dp[i-1][j-1][1] + s1[j]
				else:
						if dp[i-1][j][0] > dp[i][j-1][0]:
							dp[i][j][0] = dp[i-1][j][0]
							dp[i][j][1] = dp[i-1][j][1]
						else:
							dp[i][j][0] = dp[i][j-1][0]
							dp[i][j][1] = dp[i][j-1][1]
				if dp[i][j][0] > maxVal:
						maxVal = dp[i][j][0]
						answer = dp[i][j][1]
print(maxVal)
print(answer)