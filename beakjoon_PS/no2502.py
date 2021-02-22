import sys

D, K = map(int, sys.stdin.readline().split())

fibo = [0] * 31

fibo[1] = 1
fibo[2] = 1

for i in range(3, 31):
    fibo[i] = fibo[i-1] + fibo[i-2]

a_coe = fibo[D-2]
b_coe = fibo[D-1]

a = 0
b = 0
while True:
    a += 1
    if (K - a_coe*a) % b_coe == 0:
        b = int((K - a_coe * a) / b_coe)
        break
print(a)
print(b)
