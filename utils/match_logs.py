"""Утилита поиска события в логе.

    - требование 1
    - требование 2
    - требование N

Notes:
    концепции:
        - регулярные выражения
        - интерфейс командной строки
        - контекстный менеджер
        - исключения / exceptions
        - тестирование + tdd
        - чтение/запись файлов
        - логирование

    применение
        - re
        - argparse
        - tempfile
        - pathlib
        - doctest
        - pytest
        - logging
"""


import re
from pathlib import Path


def get_parameters():
    """Возвращает значения, переданные параметрам утилиты.

    """
    raise NotImplementedError('требуется реализация')


def get_matches(pattern: str, filename: Path) -> str:
    """Построчно читает текстовый файл.

    Возвращает строки, соответствующие шаблону.
    Если совпадений не найдено, возвращает пустой список.

    """
    results: list[str] = []

    with open(filename, 'r', encoding='utf-8') as f:
        # TODO
        # logger.info(f'открыл файл {f}')
        i: int = 1
        for line in f:
            line = line.strip()
            if re.search(pattern, line):
                # TODO
                # logger.info(f'нашел совпадение в строке {i}')
                results.append(line)
            i += 1
    return results

def get_view(data: list[str]):
    """Возвращает представление данных."""
    print(data)


if __name__ == '__main__':
    file_to_search = Path('.data/some_log.txt')
    get_view(get_matches('exciting', file_to_search))
