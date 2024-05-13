import random
from tabulate import tabulate

values = {
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4,
    'f' : 5,
    'g' : 6,
    'h' : 7
}
header = [":)", "0", "1", "2", "3", "4", "5", "6", "7"]
temp_found = []
user_values = []
progress = True
won = False

difficulty_choice = int(input("""
Choose the Difficulty:
Press (1) for Easy Mode
Press (2) for Medium Mode
Press (3) for Hard Mode
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
        random.shuffle(lst)
    return lst

if difficulty_choice == 1:
    main = game_elements(4)
    list_with_spaces = [[' ' for _ in sublist] for sublist in main]
    while progress:
        for i in range(2):
            opn = input("\nEnter the tile to uncover: ")
            user_values.append(opn)

            index_1 = values[opn[0]]
            index_2 = int(opn[1])

            temp_found.append(main[index_1][index_2])
            
            list_with_spaces[index_1][index_2] = main[index_1][index_2]
            #print(tabulate(list_with_spaces, header , showindex="always", tablefmt="rounded_grid"))
            print(tabulate(list_with_spaces, tablefmt="rounded_grid"))

        if temp_found[0] == temp_found[1]:
            for i in range(2):
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

if difficulty_choice == 2:
    main = game_elements(6)
    print(main)

if difficulty_choice == 3:
    main = game_elements(8)
    print(main)