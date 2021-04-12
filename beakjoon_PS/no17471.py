import sys, collections, itertools

def bfs1(adj, visited, people, start):
  q = collections.deque()
  q.append(start)
  visited[start] = 1
  peoples = people[start]

  while q:
    vertex = q.popleft()

    for next_vertex in adj[vertex]:
      if visited[next_vertex] == 0:
        visited[next_vertex] = 1
        peoples += people[next_vertex]
        q.append(next_vertex)
        

  return [visited, peoples]

def bfs2(adj, visited, case, anti_case, start):
  q = collections.deque()
  q.append(start)
  visited[start] = 1

  while q:
    vertex = q.popleft()

    if vertex not in anti_case:
      for next_vertex in adj[vertex]:
        if visited[next_vertex] == 0:
          visited[next_vertex] = 1
          q.append(next_vertex)
        
  judge = True

  for vertex in case:
    if visited[vertex] == 0:
      judge = False
      break
  
  return judge

n = int(sys.stdin.readline())
people = [0] + list(map(int, sys.stdin.readline().split()))
adj = [[] for _ in range(n+1)]

for i in range(1, n+1):
  temp = list(map(int, sys.stdin.readline().split()))
  sections = temp[1:]

  for section in sections:
    adj[i].append(section)

elections = 0
visited = [0] * (n+1)
peoples_list = []


for i in range(1, n+1):
  if visited[i] == 0:
    temp = bfs1(adj, visited, people, i)
    visited, peoples = temp[0], temp[1]
    peoples_list.append(peoples)
    elections += 1

if elections == 1:
  min_value = sys.maxsize
  vertexes = [i for i in range(1,n+1)]
  sum_value = 0

  for vertex in vertexes:
    sum_value += people[vertex]

  for i in range(1, n):
    cases = itertools.combinations(vertexes, i)
    

    for case in cases:
      case = list(case)
      case_sum_value = 0
      anti_case = []

      for vertex in vertexes:
        if vertex not in case:
          anti_case.append(vertex)

      visited = [0] * (n+1)
      case_judge = bfs2(adj, visited, case, anti_case, case[0])
      visited = [0] * (n+1)
      anti_case_judge= bfs2(adj, visited, anti_case, case, anti_case[0])

      if case_judge and anti_case_judge:
        for vertex in case:
          case_sum_value += people[vertex]

        min_value = min(min_value, abs(case_sum_value - (sum_value-case_sum_value)))

  print(min_value)
  

elif elections == 2:
  print(abs(peoples_list[0] - peoples_list[1]))

else:
  print(-1)
