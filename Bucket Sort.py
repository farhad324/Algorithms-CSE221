def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up    
    return b    
             
def bucketSort(A):
    n=len(A)
    arr = []
    for i in range(n):
        arr.append([])    
    for i in range(0,n):
        arr[int(n*A[i])].append(A[i])

    for i in range(0,n):
        arr[i] = insertionSort(arr[i])
   
       
    k = 0
    for i in range(n):
        for j in range(len(arr[i])):
            A[k] = arr[i][j]
            k += 1
    return A
 

x= [0.77,0.16,0.39,0.26,0.71,0.95,0.21,0.12,0.23,0.68]

print("Sorted Array is:",bucketSort(x))


## OUTPUT:

'''
Sorted Array is: [0.12, 0.16, 0.21, 0.23, 0.26, 0.39, 0.68, 0.71, 0.77, 0.95]

'''
