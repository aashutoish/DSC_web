# Sorting Algorithms

# 1. Bubble Sort - compares adjacent elements and swaps if out of order
def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


# 2. Insertion Sort - builds sorted array one element at a time
def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# 3. Selection Sort - finds minimum and places in correct position
def selection_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


# 4. Merge Sort - divide and conquer using recursive merging
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# 5. Quick Sort - partition-based divide and conquer
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)


# 6. Heap Sort - build max heap and extract elements
def heap_sort(arr):
    a = arr[:]
    n = len(a)
    
    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and a[left] > a[largest]:
            largest = left
        if right < n and a[right] > a[largest]:
            largest = right
        
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(n, largest)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(i, 0)
    
    return a

# Test the sorting algorithms
if __name__ == "__main__":
    data1 = [64, 34, 25, 12, 22, 11, 90]
    print("Bubble Sort:", bubble_sort(data1))
    print("Insertion Sort:", insertion_sort(data1))
    print("Selection Sort:", selection_sort(data1))
    print("Merge Sort:", merge_sort(data1))
    print("Quick Sort:", quick_sort(data1))
    print("Heap Sort:", heap_sort(data1))
    
    print("\nReverse sorted:")
    data2 = [7, 6, 5, 4, 3, 2, 1]
    print("Bubble Sort:", bubble_sort(data2))
    print("Merge Sort:", merge_sort(data2))
    print("Quick Sort:", quick_sort(data2))
    
    print("\nWith duplicates:")
    data3 = [5, 3, 8, 3, 1, 5, 8]
    print("Bubble Sort:", bubble_sort(data3))
    print("Heap Sort:", heap_sort(data3))
