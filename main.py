import os

MOVES = {"a1": "-", "a2": "-", "a3": "-",
         "b1": "-", "b2": "-", "b3": "-",
         "c1": "-", "c2": "-", "c3": "-"}

tic_tac_toe = f"""
       1     2     3
     _____ _____ _____
    |     |     |     |
 a  |  {MOVES["a1"]}  |  {MOVES["a2"]}  |  {MOVES["a3"]}  |
    |_____|_____|_____|
    |     |     |     |
 b  |  {MOVES["b1"]}  |  {MOVES["b2"]}  |  {MOVES["b3"]}  |
    |_____|_____|_____|
    |     |     |     |
 c  |  {MOVES["c1"]}  |  {MOVES["c2"]}  |  {MOVES["c3"]}  |
    |_____|_____|_____|
"""

print(tic_tac_toe)
print("Welcome to tic-tac-toe! \n")

move_no = 1


def clear_screen():
    return os.system('cls')


def move():
    current_turn = True
    global move_no
    if move_no % 2 != 0:
        symbol = "X"
    else:
        symbol = "O"
    while current_turn:
        move = input(f"Indicate the position where you want to make your move. Eg. a1\n{symbol} Turn: ").lower()
        if move in MOVES.keys():
            if MOVES[move] == "-":
                MOVES[move] = symbol
                move_no += 1
                print(f"""
                       1     2     3
                     _____ _____ _____
                    |     |     |     |
                 a  |  {MOVES["a1"]}  |  {MOVES["a2"]}  |  {MOVES["a3"]}  |
                    |_____|_____|_____|
                    |     |     |     |
                 b  |  {MOVES["b1"]}  |  {MOVES["b2"]}  |  {MOVES["b3"]}  |
                    |_____|_____|_____|
                    |     |     |     |
                 c  |  {MOVES["c1"]}  |  {MOVES["c2"]}  |  {MOVES["c3"]}  |
                    |_____|_____|_____|
                """)
                current_turn = False
            else:
                print("Choose another place as the last one is already used.")
        else:
            print("Incorrect Position")


def check_if_winner():
    winning_combos = [
        [MOVES["a1"], MOVES["a2"], MOVES["a3"]], [MOVES["b1"], MOVES["b2"], MOVES["b3"]],
        [MOVES["c1"], MOVES["c2"], MOVES["c3"]],
        [MOVES["a1"], MOVES["b1"], MOVES["c1"]], [MOVES["a2"], MOVES["b2"], MOVES["c2"]],
        [MOVES["a3"], MOVES["b3"], MOVES["c3"]],
        [MOVES["a1"], MOVES["b2"], MOVES["c3"]], [MOVES["a3"], MOVES["b2"], MOVES["c1"]]
    ]
    for combo in winning_combos:
        winner_x = all(element == "X" for element in combo)
        winner_o = all(element == "O" for element in combo)
        if winner_x:
            print("~~~~~~~~~~~~~~~~~~ X Won! ~~~~~~~~~~~~~~~~~~")
            return True
        elif winner_o:
            print("~~~~~~~~~~~~~~~~~~ O Won! ~~~~~~~~~~~~~~~~~~")
            return True


game_is_on = True

while game_is_on:
    if move_no > 9:
        print("~~~~~~~~~~~~~~~~~~ It is s tie! ~~~~~~~~~~~~~~~~~~")
    move()
    if check_if_winner():
        game_is_on = False
    else:
        clear_screen()


