# Пузырьковая сортировка
#nums = [5,6,2,1,3,4]
def bubble_sort(ls):
    for i in range(i):
        if ls[j] > ls[j + 1]:
            ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls

#Сортировка выборкой
def selection_sort(ls):
    for i in range(len(ls) - 1):
        min_index = i
        for j in range(i + 1, len(ls)):
            if ls[min_index] > ls[j]:
                min_index = j
                ls[min_index], ls[j] = ls[j], ls[min_index]
    return ls

#Сортировка вствкой
def insertion_sort(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
            ls[j + 1] = key
    return ls
