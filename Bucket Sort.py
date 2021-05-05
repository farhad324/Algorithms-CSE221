def insertionSort(element_array):
    for i in range(1, len(element_array)):
        key = element_array[i]
        j = i - 1
        while j >= 0 and element_array[j] > key:
            element_array[j + 1] = element_array[j]
            j -= 1
        element_array[j + 1] = key    
    return element_array

def bucketSort(array):
    bucket = []

    for i in range(len(array)):
        bucket.append([])

    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    for i in range(len(array)):
        bucket[i] = insertionSort(bucket[i])

    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


array = [.44, .39, .33, .21, .51, .47, .51]
sorted_array = bucketSort(array)
print("Sorted Array:",sorted_array)

## OUTPUT:

'''
Sorted Array: [0.21, 0.33, 0.39, 0.44, 0.47, 0.51, 0.51]

'''
