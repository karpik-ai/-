import json  # Добавляем модуль данных json


def task() -> float:
    with open('input.json', "r") as input_file:  # Открываем файл в формате чтения
        data = json.load(input_file)  # Дисериализация

    list_of_values = sum([(number["score"] * number["weight"]) for number in data])
    # Ищем сумму произведений
    return round(list_of_values, 3)
    # Вовзращаем значение функции, округленное до 3 знаков


print(task())
