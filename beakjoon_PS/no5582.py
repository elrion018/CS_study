import sys

s1 = list(sys.stdin.readline().strip())
s2 = list(sys.stdin.readline().strip())
maxVal = 0

dp = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]

for i in range(1,len(s2)+1):
		for j in range(1,len(s1)+1):
				if s2[i-1] == s1[j-1]:
						dp[i][j] = dp[i-1][j-1]+1
						maxVal = max(maxVal, dp[i][j])
print(maxVal)