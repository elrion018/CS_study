import sys
import fractions
N = int(sys.stdin.readline())
rings = list(map(int, sys.stdin.readline().split()))
first_ring = rings[0]
rings = rings[1:]

for ring in rings:
    temp = fractions.Fraction(first_ring, ring)
    if temp == int(temp):
        print(str(temp) + "/1")
    else:
        print(temp)
