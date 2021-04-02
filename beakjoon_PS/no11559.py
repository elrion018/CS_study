import sys
import collections


def search_same_puyo(board, visited, sty, stx):
  puyo = board[sty][stx]
  q = collections.deque()
  q.append([sty, stx])
  visited[sty][stx] = 1
  trace = [[sty, stx]]

  dy = [0, 0, 1, -1]
  dx = [1, -1, 0, 0]

  while q:
    by, bx = q.popleft()

    for i in range(4):
      ay = by + dy[i]
      ax = bx + dx[i]

      if ay >= 0 and ay < 12 and ax >= 0 and ax <6:

        if board[ay][ax] == puyo and visited[ay][ax] == 0:
          q.append([ay, ax])
          trace.append([ay,ax])
          visited[ay][ax] = 1

  return trace, visited

def brute_force_for_delete_puyo(board):
  visited = [[0] * 6 for _ in range(12)]
  delete_count = 0
  
  for y in range(12):
    for x in range(6):
      if board[y][x] != '.' and visited[y][x] == 0:
        trace, visited = search_same_puyo(board, visited, y, x)
        delete_count += delete_puyo(board, trace)
        

  return board, delete_count

def delete_puyo(board, trace):
  delete_count = 0

  if len(trace) >= 4:
    for y, x in trace:
      board[y][x] = '.'
      delete_count += 1


  return delete_count

def brute_force_for_move_down_puyo(board):
  for y in range(11, -1, -1):
    for x in range(5, -1, -1):
      if board[y][x] != '.':
        board = move_down_puyo(board, y, x)

  return board

def move_down_puyo(board, py, px):
  sty = py
  puyo = board[sty][px]

  while valid_puyo_move(board, py,px):
    py += 1

  board[sty][px] = '.'
  board[py][px] = puyo

  return board


def valid_puyo_move(board, py, px):
  if py+1 > 11 or board[py+1][px] != '.':
    return False

  return True

def solution(board):
  count = 0
  judge = True

  while judge:
    board, delete_count = brute_force_for_delete_puyo(board)
    board = brute_force_for_move_down_puyo(board)

    if delete_count == 0:
      judge = False
      
    else:
      count += 1
  
  return count



board = [list(sys.stdin.readline().strip()) for _ in range(12)]

print(solution(board))

