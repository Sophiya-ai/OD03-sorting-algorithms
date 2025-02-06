# Быстрая сортировка использует метод «разделяй и властвуй». Она выбирает опорный элемент (pivot) и
# разделяет массив на две части: элементы меньше опорного и элементы больше опорного.
# Затем сортировка применяется рекурсивно к каждой части.

def quick_sort(s):
    if len(s) <= 1:
        return s
    pivot = s[0]
    left = list(filter(lambda i: i < pivot, s))
    center = [i for i in s if i == pivot]
    right = list(filter(lambda i: i > pivot, s))

    return quick_sort(left) + center + quick_sort(right)

print(quick_sort([9, 0, 1, 5, 3, 7, 9]))
