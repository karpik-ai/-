salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0  # Вводим начальную подушку безопасности для дальннейших расчетов

for month in range(months):
    if month > 0:  # Берем значение больше нуля, так как в первый месяц увеличения расходов нет
        spend *= 1+increase
    if spend > salary:
        money_capital += (spend - salary)  # Считаем финансовую подушку если расходы больше доходов
        money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
