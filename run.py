import random

class PythonBattleships:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board_size = 0
        self.num_ships = 0
        self.user_board = []
        self.computer_board = []
        self.user_ships = []
        self.computer_ships = []
        
        if self.difficulty == "easy":
            self.board_size = 2
            self.num_ships = 2
        elif self.difficulty == "medium":
            self.board_size = 8
            self.num_ships = 8
        elif self.difficulty == "hard":
            self.board_size = 12
            self.num_ships = 12
        
