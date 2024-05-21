import random
from tabulate import tabulate
import os

values = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7}
temp_found = []
user_values = []
user_choices = []
progress = True
competed = False

user_choice_data = int(input("""
Eg1:- for '2x2' enter 2
Eg2:- for '4x4' enter 4       
NOTE:- Enter only EVEN numbers

Enter your choice: """))

while (user_choice_data%2) != 0:
    os.system("cls")
    user_choice_data = int(input("""
Eg1:- for '2x2' enter 2
Eg2:- for '4x4' enter 4            
NOTE:- Enter only EVEN numbers

Enter your choice: """))

def game_elements(num):
    lst = []
    while len(lst) < num:
        row = []
        while len(row) < num:
            random_number = random.randint(1,10)
            if random_number not in row:
                row.append(random_number)
        lst.append(row)
        element = row.copy()
        random.shuffle(element)
        lst.append(element)
    return lst

def game_process(num):
    global user_values
    global temp_found
    global competed

    list_with_spaces = [[' ' for _ in sublist] for sublist in main]
    while progress:
        os.system('cls')
        print(tabulate(list_with_spaces, tablefmt="rounded_grid"))
        trial = 0
        for i in range(2):
            if len(user_choices) == (num**2):
                competed = True
                break

            opn = input("\nEnter the tile to uncover: ")
            while opn in user_choices:
                print("\n===========>>>You have already completed this tile!")
                opn = input("\nEnter the new tile to uncover: ")
            user_values.append(opn)

            index_1 = values[opn[0]]
            index_2 = int(opn[1])

            temp_found.append(main[index_1][index_2])
            
            list_with_spaces[index_1][index_2] = main[index_1][index_2]
            print(tabulate(list_with_spaces, tablefmt="rounded_grid"))
            trial += 1
            if trial == 2:
                user_input = input("\n===========>>> Press (Enter) to Continue: ")
                trial = 0

        if competed:
            print("\n===========>>> You Won! <<<===========")
            break
        elif temp_found[0] == temp_found[1]:
            for i in range(2):
                user_choices.append(user_values[i])
                index_1 = values[user_values[i][0]]
                index_2 = int(user_values[i][1])
                list_with_spaces[index_1][index_2] = "✅"
            user_values = []
            temp_found = []
        else:
            for i in range(2):
                index_1 = values[user_values[i][0]]
                index_2 = int(user_values[i][1])
                list_with_spaces[index_1][index_2] = " "
            user_values = []
            temp_found = []
while True:
    main = game_elements(user_choice_data)
    process = game_process(user_choice_data)

    choice = input("Do you want to play the game again? (y/n): ").lower()

    while choice not in ["y", "n"]:
        print("\n Invalid choice")
        choice = input("Do you want to play the game again? (y/n): ")
    
    if choice == "n":
        break