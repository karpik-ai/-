players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle = len(players) // 2  # разбиваем список на две части

first_team = players[:middle]  # слайсирование, первая команда
second_team = players[middle:]  # слайсировние, пвторая команда

print(first_team)
print(second_team)
