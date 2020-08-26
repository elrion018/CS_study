# D[i] = N이 i일때 지원이가 만들 수 있는 모든 가짓 수
# D[i] = D[i-2] + D[i-1]
import sys
N = int(sys.stdin.readline())


first = 1
second = 2

for i in range(N-1):
    third = first + second
    first = second
    second = third % 15746
print(first)
