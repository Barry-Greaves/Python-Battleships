import random

class PythonBattleships:
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
            self.num_ships = 2
        elif self.difficulty == "medium":
            self.board_size = 6
            self.num_ships = 6
        elif self.difficulty == "hard":
            self.board_size = 8
            self.num_ships = 8
    
    def create_player_board(self):
        """
        Create battleships board for the player
        """
        for i in range(self.board_size):
            self.player_board.append([])
        for j in range(self.board_size):
            self.player_board[i].append(".")

    def create_computer_board(self):
        """
        Create battleships board for the computer
        """
        for i in range(self.board_size):
            self.computer_board.append([])
        for j in range(self.board_size):
            self.computer_board[i].append(".")

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
        
    
        
