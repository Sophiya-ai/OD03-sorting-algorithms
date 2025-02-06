# Сортировка выбором работает путем поиска минимального элемента в неотсортированной части массива
# и его обмена с первым элементом этой части. Затем процесс повторяется для оставшейся части массива.

a = [-3, 5, 0, -8, 1, 10]


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


selection_sort(a)
print(a)
