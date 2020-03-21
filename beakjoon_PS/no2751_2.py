# def merge_sort(arr):
#     if len(arr) == 1:
#         return arr
#     mid = len(arr) // 2
#     left_arr = merge_sort(arr[:mid])
#     right_arr = merge_sort(arr[mid:])
#     return merge(left_arr, right_arr)


# def merge(left_arr, right_arr):
#     result = []
#     while len(left_arr) > 0 or len(right_arr) > 0:
#         if len(left_arr) > 0 and len(right_arr) > 0:
#             if left_arr[0] <= right_arr[0]:
#                 result.append(left_arr[0])
#                 left_arr = left_arr[1:]
#             else:
#                 result.append(right_arr[0])
#                 right_arr = right_arr[1:]
#         elif len(left_arr) > 0:
#             result.append(left_arr[0])
#             left_arr = left_arr[1:]

#         elif len(right_arr) > 0:
#             result.append(right_arr[0])
#             right_arr = right_arr[1:]

#     return result


N = int(input())

arr = [int(input()) for _ in range(N)]

# results = merge_sort(arr)
results = sorted(arr)
for i in results:
    print(i)
