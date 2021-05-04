def interpolationSearch(array, x):
 
    (left, right) = (0, len(array) - 1)
 
    while array[right] != array[left] and array[left] <= x <= array[right]:
 
        mid = left + (x - array[left]) * (right - left) // (array[right] - array[left])
 
        if x == array[mid]:
            return mid

        elif x < array[mid]:
            right = mid - 1
 

        else:
            left = mid + 1
 
    if x == array[left]:
        return left
 
    return -1
 
 

array = [2, 5, 6, 8, 9, 10]
key = 6
 
index = interpolationSearch(array, key)
 
if index != -1:
    print("Element found at index", index)
else:
    print("Element found not in the list")