import random
def find():
    while True:
        random_n = [random.randint(0, 200) for _ in range(10)]
        print(f"Сгенерированный список чисел: {random_n}")

        try:
            x = input("Введите число X: ")
            
            if not x.isdigit() or int(x) <= 0:
                print("Ошибка: Введите целое положительное число.")
                continue  # Возвращаемся к следующему запросу

            x = int(x)

            multiples = list(filter(lambda num: num % x == 0, random_n))

            if multiples:
                print(f"Числа, кратные {x}: {multiples}")
            else:
                print(f"Нет чисел, кратных {x}.")
        
        except ValueError:
            print("Ошибка: Введите корректное число.")
find()
