

def quick_sort(array):
    array_length = len(array)
    if array_length <= 1:
        return array

    else:
        pivot = array[0]

        greater = [element for element in array[1:] if element > pivot]
        lesser = [element for element in array[1:] if element <= pivot]

        return quick_sort(greater) + [pivot] + quick_sort(lesser)


print(''.join(quick_sort(list(input()))))
