numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90,
           -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missed_number = 4  # обозначаем пропущенное число
next_number = 5  # обозначем следующее число
list_without_missed_number =\
    numbers[:missed_number] + numbers[next_number:]
# формируем новый список
average = sum(list_without_missed_number) / len(numbers)
# ищем среднее значение
numbers[missed_number] = average
# даем пропущенному элементу значение

print("Измененный список:", numbers)
