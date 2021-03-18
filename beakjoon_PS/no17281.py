import sys, itertools

n = int(sys.stdin.readline())
results = [0] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(n)]
temp = [2,3,4,5,6,7,8,9]
orders = list(itertools.permutations(temp, 8))
ans = 0

for order in orders:
  order = [0] + list(order)
  order.insert(4, 1)
  score = 0
  idx = 1

  for k in range(1,n+1):
    first_base, second_base, third_base = 0, 0, 0
    home = 0
    out = 0
    start = idx # 이닝이 바뀌어도 타순은 유지되므로

    while out <3: # 3아웃 되기 전까지 무한루프
      for i in range(start, len(order)):

          if results[k][order[i]] == 1: # 안타
            home += third_base
            first_base, second_base, third_base = 1, first_base, second_base

          elif results[k][order[i]] == 2: #2루타
            home += (third_base + second_base)
            first_base, second_base, third_base = 0, 1, first_base

          elif results[k][order[i]] == 3: #3루타
            home += (first_base + second_base + third_base)
            first_base, second_base, third_base = 0, 0, 1

          elif results[k][order[i]] == 4: #홈런
            home += (1+ first_base + second_base + third_base)
            first_base, second_base, third_base = 0, 0, 0

          elif results[k][order[i]] == 0: #아웃
            out += 1

            if out == 3: # 3아웃이라면
              if i + 1 == 10:
                idx = 1

              else:
                idx = i + 1 # 마지막으로 아웃한 선수 다음 선수가 다음 이닝 타자

              break

      start= 1 # 타순 초기화
      
    score += home # 이닝 끝 점수 누적

  ans = max(ans, score)
  
print(ans)
