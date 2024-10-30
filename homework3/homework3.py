from datetime import datetime
print("Выполнил Вахитов Данис ПИ-332Б")
def calculate_age():
    today = datetime.today()
    print(f"Текущая дата: {today.strftime('%d/%m/%Y')}")
    b_date_str = input("Введите дату рождения в формате дд.мм.гггг: ")
    if not all(char.isdigit() or char == '.' for char in b_date_str.replace(".", "")):
        print("Ошибка: Дата должна содержать только целые числа и символ '.'.")
        return
    try:
        day, month, year = b_date_str.split('.')

        if not (day.isdigit() and month.isdigit() and year.isdigit()):
            print("Ошибка: В дате должны быть только целые числа.")
            return

        day, month, year = int(day), int(month), int(year)

        if day <= 0 or month <= 0 or year <= 0:
            print("Ошибка: День, месяц и год должны быть положительными числами.")
            return

        b_date = datetime(year, month, day)

        if b_date > today:
            print("Ошибка: Дата рождения не может быть в будущем.")
            return

        age = today.year - b_date.year
        if (today.month, today.day) < (b_date.month, b_date.day):
            age -= 1  
        print(f"Вам {age} лет.")
    
    except ValueError:
        print("Ошибка: Введите корректную дату в формате дд.мм.гггг.")
calculate_age()
