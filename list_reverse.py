def create_range_decr_2_int(max_min):
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
    num_max, num_min = list(map(int, max_min.split(", ")))
    if num_max > num_min:
        print(list(range(num_max, num_min - 1, -1)))
    else:
        print(list(range(num_min, num_max - 1, -1)))

# call function
startstop = "25, 9"
create_range_decr_2_int(startstop)
