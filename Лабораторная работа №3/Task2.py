
def find_common_participants(first_group, second_group, separator=","):  # Составляем функцию
    first_separated = first_group.split(separator)
    second_separated = second_group.split(separator)

    common_members = set(first_separated).intersection(second_separated)
    # Ищем общих участников, допольнительно используем функцию set
    new_common_members = list(common_members)  # Переводим в список
    new_common_members.sort()  # Сортируем

    return new_common_members


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


common_participants = find_common_participants(participants_first_group,
                                               participants_second_group, "|")  # Нстандартный разделитель
print(common_participants)
