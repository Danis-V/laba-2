print("Генератор:")
def my_generate(start=0, stop=6, step=1):
    number = start
    while number <= stop:
        yield number
        number += start
ranger = my_generate(1,5)
for value in ranger:
    print(value)
