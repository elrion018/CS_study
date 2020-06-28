import sys

arr = [int(sys.stdin.readline()) for _ in range(10)]
results = []
for i in arr:
    results.append(i % 42)
print(len(set(results)))
