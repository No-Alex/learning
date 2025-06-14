# преобразовать произвольное число минут (возможно, более 1 суток) в показания цифровых часов
# TODO - переименовать по-питоновски модуль и идентификаторы
# В Python преимущественно используется нотация under_score
total_minutes = int(12305)

watch_minutes = total_minutes % 60
full_days = total_minutes // (60*24)
watch_hours = (total_minutes // 60) - (full_days*24)
# добавить добивку нулями слева
s_watch_hours = "0" + str(watch_hours)
s_watch_hours = s_watch_hours[-2:]
s_watch_minutes = "0" + str(watch_minutes)
s_watch_minutes = s_watch_minutes[-2:]
actual = s_watch_hours + ':' + s_watch_minutes
print(actual)
expected = "13:05"
assert actual == expected
print("Test passed")

expected = "13:35"
assert actual == expected
print("Test passed")