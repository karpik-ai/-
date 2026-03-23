def items(list_, product):  # Создаем функцию

    for index, j in enumerate(list_):  # Задаем нумерованный список
        if j == product:
            return index


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = items(items_list, find_item)  # Возвращаем раннее заданную функцию
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")  # Случай когда товар не найден в списке
