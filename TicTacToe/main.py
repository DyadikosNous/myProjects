board = [' ' for _ in range(9)]

# Εμφάνιση πίνακα
def display_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Έλεγχος Νικητή
def check_winner(symbol):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    for combination in winning_combinations:
        # Έλεγχος αν κάθε θέση που νικάει καλύπτεται απο το ίδιο σύμβολο
        if all(board[i] == symbol for i in combination):
            return True
    return False

# Βασική μέθοδος έναρξης παιχνιδιού
def play_game():
    current_player = 'X'
    game_over = False
    while not game_over:
        display_board()
        position = int(input("Επιλέξτε θέση (1-9): ")) - 1
        # Έλεγχος σωστής τοποθέτησης
        if board[position] == ' ':
            board[position] = current_player
            if check_winner(current_player):
                display_board()
                print("Συγχαρητήρια! Ο παίκτης", current_player, "κέρδισε!")
                game_over = True
            elif ' ' not in board:
                display_board()
                print("Ισοπαλία!")
                game_over = True
            else:
                # Switch players
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Λάθος κίνηση! Ξαναπροσπαθήστε")

# Start the game
play_game()
