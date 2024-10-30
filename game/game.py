import random
print("Выполнил Вахитов Данис ПИ-332Б")
def d_winner(player, computer):
    if player == computer:
        print('Ничья!')
    elif (player == 1 and computer == 2) or \
         (player == 2 and computer == 3) or \
         (player == 3 and computer == 1):
        print('Победа!')
    else:
        print('Поражение...')

def game():
    while True:
        print("\nВыберите 1 - Ножницы, 2 - Бумага, 3 - Камень,'0' - Выход): ")
        
        player_in = input()  
        if player_in.lower() == '0':  
            print("Спасибо за игру!")
            break
        
        if not player_in.isdigit() or int(player_in) not in (1, 2, 3):  
            print('Некорректный ввод! Попробуйте снова.')
            continue
        
        player = int(player_in)  
        computer = random.randint(1, 3)
        
        if computer == 1:
            print('Компьютер выбрал ножницы')
        elif computer == 2:
            print('Компьютер выбрал бумагу')
        else:
            print('Компьютер выбрал камень')
        d_winner(player, computer)
game()
