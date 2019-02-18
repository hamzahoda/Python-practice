def merge_sort(sequence):
    if len(sequence) < 2:
        return sequence
    m = len(sequence) // 2
    return merge(merge_sort(sequence[:m]), merge_sort(sequence[m:]))

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result

def selection_sort(sequence):  
    for i in range(len(sequence)):           
        index= i
        for j in range(i+1, len(sequence)): 
            if sequence[index] > sequence[j]: 
                index = j                  
        sequence[i], sequence[index] = sequence[index], sequence[i] 
    return sequence

def bubble_sort(sequence): 
    n = len(sequence) 
    for i in range(n):
        for j in range(0, n-i-1): 
            if sequence[j] > sequence[j+1] : 
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
    return sequence

#print (merge_sort([5, 2,-3, 6, 8, 5, 8, 1]))
#print (selection_sort([5, 2,-3, 6, 8, 5, 8, 1]))
#print (bubble_sort([5, 2,-3, 6, 8, 5, 8, 1]))
