import sys

def judge_operation(arr):
		
		if len(arr) >= len(arr[0]):
			return 'R'

		else:
			return 'C'

def sort_opertion(arr, operation):
		if operation == 'R':
			operated_arr = r_operation(arr)
		elif operation == 'C':
			operated_arr = c_operation(arr)

		return operated_arr
		

def dic_to_list(arr):
		dic_converted_list = []
		temp = sorted(list(arr.items()), key = lambda element: (element[1], element[0]))

		for i in range(len(temp)):
			for j in range(2):
				dic_converted_list.append(temp[i][j])
	
		if len(dic_converted_list) > 100:
			return dic_converted_list[:100]

		return dic_converted_list

def r_operation(arr):
		dic = dict()
		max_length = 0
		number_and_count_arr = []

		for y in range(len(arr)):
			for x in range(len(arr[0])):
				if arr[y][x] != 0:
					if arr[y][x] in dic:
						dic[arr[y][x]] += 1
					else:
						dic[arr[y][x]] = 1

			dic_converted_list = dic_to_list(dic)
			max_length = max(max_length, len(dic_converted_list))
			number_and_count_arr.append(dic_converted_list)
			dic = dict()

		operated_arr = [[0]*(max_length) for _ in range(len(number_and_count_arr))]

		for y in range(len(number_and_count_arr)):
			for x in range(len(number_and_count_arr[y])):
				operated_arr[y][x] = number_and_count_arr[y][x]


		return operated_arr


def c_operation(arr):
		dic = dict()
		max_length = 0
		number_and_count_arr = []

		for x in range(len(arr[0])):
			for y in range(len(arr)):
				if arr[y][x] != 0:
					if arr[y][x] in dic:
						dic[arr[y][x]] += 1
					else:
						dic[arr[y][x]] = 1
			
			dic_converted_list = dic_to_list(dic)
			max_length = max(max_length, len(dic_converted_list))


			number_and_count_arr.append(dic_converted_list)
			dic = dict()

		operated_arr = [[0]*(len(number_and_count_arr)) for _ in range(max_length)]

		for y in range(len(number_and_count_arr)):
			for x in range(len(number_and_count_arr[y])):
				operated_arr[x][y] = number_and_count_arr[y][x]
				
		return operated_arr



def solution(r,c,k, arr):
		time = 0
		while True:
			if len(arr) >= r and len(arr[0]) >= c and arr[r-1][c-1] == k:
				return time
			if time > 100:
				return -1

			operation = judge_operation(arr)
			operated_arr = sort_opertion(arr, operation)
			arr = operated_arr
			time += 1
			

r, c, k = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

print(solution(r,c,k,arr))