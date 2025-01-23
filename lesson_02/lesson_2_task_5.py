def month_to_season(month):
    if month in [12, 1, 2]:
        return "Время года - Зима"
    elif month in [3, 4, 5]:
        return "Время года - Весна"
    elif month in [6, 7, 8]:
        return "Время года - Лето"
    elif month in [9, 10, 11]:
        return "Время года - Осень"
    else:
        return "Такого месяца не существует"


month = int(input("Введите месяц "))
season = month_to_season(month)


print(f"Месяц {month} относится к сезону: {season}")
