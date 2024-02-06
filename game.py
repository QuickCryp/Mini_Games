import random
import time

class Games:
    def __init__(self):
        self.start_x = 0 # откуда будет начинатся x
        self.end_x = 0 # где будет заканчиваться x
        self.amount_of_game = None
        self.random_x_value = random.uniform(self.start_x, self.end_x)
        self.user_x = None
        self.counter = 0
        self.balance = 0 # баланс пользователя
        self.commands = [
            'crash', 'another game', 'admin menu'
        ] # команды пользователя
    
    def enter_command(self):
        print('''
        WELCOME TO CRASH GAME!\nDeveloped by https://randomlywebban.t.me
                ''')
        choice = input('Enter command(word)\n[1] Crash\n[2] Another Game\n[3] Admin Menu\nEnter Word: ')
        if choice.lower() == 'crash':
            game = Games()
            game.crash_game()
        elif choice.lower() == 'admin menu':
            print('Admin panel in future!')
        elif choice.lower() == 'another game':
            game = Games()
            game.another_game()
        else:
            print('No such command! Try again')


    def another_game(self):
        print('''
        U IN ANOTHER GAME MENU\nDeveloped by https://randomlywebban.t.me''')
        print(f'''
        Its Ur menu of another game
        Ur balance is: {self.balance}''')
        

    def crash_game(self):
        print('''
        U IN CRASH GAME MENU\nDeveloped by https://randomlywebban.t.me''')
        print(f'''
        Its Ur menu of crash game\nUr balance is: {self.balance}''')
        max_attempts = 999999999999999 # оставьте)
        self.user_x = float(input("Enter ur bid: "))
        self.amount_of_game = int(input('Enter ur bid amount: '))
        for attempt in range(max_attempts):
            if self.random_x_value >= self.user_x:
                time.sleep(2)
                if self.user_x != 0:
                    self.balance += self.amount_of_game * self.user_x
                print('U win!')
                print(f'Ur balance is {self.balance}')
                
            else:
                time.sleep(2)
                if self.balance >= self.amount_of_game:
                    self.balance -= self.amount_of_game
                    print('U lose!')
                    print(f'Ur balance is {self.balance}')
                else:
                    print("Not enough balance to continue. Game over.")
                    break

            if attempt < max_attempts - 1:
                f = input('Do you want to continue? Type y/N/menu: ')
                if f.lower() == 'y':
                    game = Games()
                    game.crash_game()
                elif f.lower() == 'menu':
                    game = Games()
                    game.enter_command()
                else:
                    self.user_x = float(input("Enter ur bid: "))
                    self.amount_of_game = int(input('Enter ur bid amount: '))
            else:
                print("Max attempts reached. Game over.")


game = Games()
game.enter_command()