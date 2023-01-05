import random


class PythonBattleships:
    """
    Contruct game class that defines difficulty level,
    board size and number of ships
    """
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board_size = 0
        self.num_ships = 0
        self.player_board = []
        self.computer_board = []
        self.hidden_computer_board = []
        self.player_ships = []
        self.computer_ships = []
        
        if self.difficulty == "easy":
            self.board_size = 2
            self.num_ships = 1
        elif self.difficulty == "medium":
            self.board_size = 6
            self.num_ships = 6
        elif self.difficulty == "hard":
            self.board_size = 8
            self.num_ships = 8
    
        self.create_player_board()
        self.place_ships_player()
        self.create_computer_board()
        self.place_ships_computer()


    def create_player_board(self):
        """
        Create battleships board for the player
        """
        for i in range(self.board_size):
            self.player_board.append(["."] * self.board_size)

    def create_computer_board(self):
        """
        Create battleships board for the computer
        """
        for i in range(self.board_size):
            self.computer_board.append(["."] * self.board_size)
            self.hidden_computer_board.append(["."] * self.board_size)

    def place_ships_player(self):
        """
        Place ships on the player's board"
        """
        for i in range(self.num_ships):
            placed = False
            while not placed:
                row = random.randint(0, self.board_size - 1)
                col = random.randint(0, self.board_size - 1)
                if self.player_board[row][col] == ".":
                    self.player_ships.append((row, col))
                    self.player_board[row][col] = "S"
                    placed = True

    def place_ships_computer(self):
        """
        Place ships on computer's hidden board so the player cannot see them"
        """
        for i in range(self.num_ships):
            placed = False
            while not placed:
                row = random.randint(0, self.board_size - 1)
                col = random.randint(0, self.board_size - 1)
                if self.hidden_computer_board[row][col] == ".":
                    self.computer_ships.append((row, col))
                    self.hidden_computer_board[row][col] = "S"
                    placed = True

    def check_shot_player(self, row, col):
        """
        Check if the player's shot has hit one of the computer's battleships
        """
        if (row, col) in self.player_ships:
            self.computer_board[row][col] = "X"
            self.hidden_computer_board[row][col] = "X"
            return True
        else:
            self.computer_board[row][col] = "M"
            self.hidden_computer_board[row][col] = "M"
            return False

    def check_shot_computer(self, row, col):
        """
        Check if the player's shot has hit one of the computer's battleships
        """
        if (row, col) in self.player_ships:
            self.player_board[row][col] = "X"
            return True
        else:
            self.player_board[row][col] = "M"
            return False

    def check_win_player(self):
        """
        Check if the player has won the game
        """
        for row in self.hidden_computer_board:
            if "S" in row:
                return False
        return True

    def check_win_computer(self):
        """
        Check if the computer has won the game
        """
        for row in self.player_board:
            if "S" in row:
                return False
        return True

    def print_player_board(self):
        """
        Prints player's board to CLI
        """
        print("Your board:")
        for row in self.player_board:
            print(" ".join(row))

    def print_computer_board(self):
        """
        Prints computer's board to CLI
        """
        print("Computer's board:")
        for row in self.computer_board:
            print(" ".join(row))

    def computers_turn(self):
        """
        Creates a random shot for the computer to take at the player
        """
        row = random.randint(0, self.board_size - 1)
        col = random.randint(0, self.board_size - 1)
        return row, col

def main():
    """
    Main function which initializes the game loop
    """
    print("Welcome to Pyhton Battleships")
    play = input("Would you like to play a game of battleships? (y/n) ")
    if play.lower() == "n":
        print("Goodbye!")
        exit()

    difficulty = input("Please select a difficulty level (easy, medium, hard): ")
    game = PythonBattleships(difficulty)
    game.create_player_board()
    game.create_computer_board()
    game.place_ships_player()
    game.place_ships_computer()

    while True:
        game.print_player_board()
        row = int(input("Enter row for shot: "))
        col = int(input("Enter column for shot: "))
        if game.check_shot_computer(row, col):
            print("Hit!")
        else:
            print("Miss!")
        if game.check_win_player():
            print("You win!")
            break
        row, col = game.computers_turn()
        if game.check_shot_player(row, col):
            print("The computer hit your ship at {} {}!".format(row, col))
        else:
            print("The computer missed your ship at {} {}!".format(row, col))
        if game.check_win_computer():
            print("The computer wins!")
            break


main()
        
    
        
