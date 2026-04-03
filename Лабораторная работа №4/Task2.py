import json  # Добавляем модуль данных json
import csv  # Добавляем модуль данных csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as input_file:  # Открываем файл в формате чтения
        lines = [row for row in csv.DictReader(input_file)]  # Используем метод DictReader

    with open(OUTPUT_FILENAME, "w") as output_file:  # Открываем файл в формате редактирования
        json.dump(lines, output_file, indent=4)  # Записываем данные в файл с отступами


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
