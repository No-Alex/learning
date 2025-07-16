"""
Дано натуральное число
Выведите его последнюю цифру
"""


def get_last_digit(num: int) -> int:
    """возвращает последнюю цифру числа
    Args:
        num: ожидается положительное целое число
    Returns: возвращает целое однозначное число
    """
    last_digit = int(str(num)[-1])
    return last_digit


print(get_last_digit(123))

if __name__ == '__main__':
    assert get_last_digit(123) == 3
