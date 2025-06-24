def create_range_decr_2_int(num_max, num_min):
    """На вход программа получает через запятую два целых числа start и stop. При этом start может быть меньше stop, а может быть больше.
    Создайте диапазон чисел с шагом 1 в обратном порядке от наибольшего числа к наименьшему (включительно). Выведите результат через запятую.

    Sample Input 1:
    0, 10
    Sample Output 1:
    10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0
    Sample Input 2:
    22, 15
    Sample Output 2:
    22, 21, 20, 19, 18, 17, 16, 15
    """
    startstop = "22, 9"
    start, stop = list(map(int, startstop.split(", ")))
    if start > stop:
        print(list(range(start, stop - 1, -1)))
    else:
        print(list(range(stop, start - 1, -1)))


create_range_decr_2_int(23, 9)
