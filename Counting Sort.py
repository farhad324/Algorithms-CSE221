def countingSort(array):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        count[array[i]] += 1

    for j in range(1,10):
        count[j] += count[j-1]

    a = size-1
    while a >= 0:
        output[count[array[a]]-1] = array[a]
        count[array[a]] -= 1
        a -= 1
    
    return output

unsorted_array = [4,2,2,2,8,8,3,3,1,7]
sorted_array=countingSort(unsorted_array)
print('Sorted Array:',sorted_array)

## OUTPUT:
'''
Sorted Array: [1, 2, 2, 2, 3, 3, 4, 7, 8, 8]

'''