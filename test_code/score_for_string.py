"""
Задача LeetCode.com #3110. Score of a String

Условие
You are given a string s. The score of a string is defined as the sum of the absolute difference between
the ASCII values of adjacent characters.
Return the score of s

Как понято
> 1. Получаем на вход строку s.
> 2. Проходим строку посимвольно от 0 до (n-2), где n-длина строки = len(s).
> 3. Для каждой пары символов i и i+1, где i-позиция в строке, определяем абсолютную разницу между
их ASCII-кодами (в какой кодировке?).
> 4. В переменной summ накапливаем сумму этих разниц.

План решения
0. Проверяем длину строки >=2. Иначе выводим ошибку и завершаем работу
1. Стандартный ввод с консоли с обрезкой строки методом .strip()
2. Организуем цикл for с итератором range от 0 до len(s)-2
2.1. Применяем функцию ord() для получения кодов соседних символов
2.2. Применяем функцию abs() для получения их разницы
2.3. Накапливаем сумму разниц в int
3. Выводим результат через print()

Перспективы
1. Определить функцию для получения абсолютной разницы двух символов (int)
2. Определить функцию для контроля длины входной строки (bool)
"""

# имитирую ввод строки
in_string = "Sm3-cE2/<]Z"
# если строка длиннее 2 символов, можно работать
if len(in_string) < 2:
    print("String too small!")
else:
    score = 0
    # range перебирает символы от первого значения до последнего включительно
    # для while следует взять len(in_string)-2
    for i in range(0, len(in_string)-1):
        # check current symbol
        print(in_string[i], ord(in_string[i]))
        score += abs(ord(in_string[i]) - ord(in_string[i+1]))
    # check last symbol
    print(in_string[i+1], ord(in_string[i+1]))
    print(f"Score of string: {score}")
