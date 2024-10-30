print("Выполнил Вахитов Данис ПИ-332Б")
def get_number0():
    for num in range(30):
        if num % 2 != 0:  
            yield num
generator = get_number0()

i=0

for value in generator:
    i+=1
    if i == 1:
        first = value
    if i == 5:
        fifth = value
    last = value  
print(f"Первое нечетное число: {first}")
print(f"Пятое нечетное число: {fifth}")
print(f"Последнее нечетное число: {last}")
