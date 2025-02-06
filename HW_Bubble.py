# Алгоритм завершится раньше, если массив уже отсортирован
    # - если во время внутреннего цикла не было произведено ни одной перестановки,
    #   алгоритм завершает выполнение, так как массив уже отсортирован

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Отсортированный массив:", sorted_arr)