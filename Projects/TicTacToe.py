###---> Tic-Tac-Toe Game <---###

import random

#Creating a Board
class Board:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        
    def print_board(self):
        print(" "+ self.board[0] +  " | " + self.board[1] +  " | " + self.board[2])
        print("-----------")
        print(" "+ self.board[3] +  " | " + self.board[4] +  " | " + self.board[5])
        print("-----------")
        print(" "+ self.board[6] +  " | " + self.board[7] +  " | " + self.board[8])
        
    def update_board(self, position, type):
        if self.board[position - 1] == " ":
            self.board[position - 1] = type
            return True
        else:
            print("Position already taken!")
            return False

#Creating a Player
class Player:
    def __init__(self,type):
        self.type = type
        self.name = self.get_name()
        
    def get_name(self):
        if self.type == "X":
            return input("Enter your name: ")
        else:
            return "Computer"

#Creating a Game
class Game:
    def __init__(self):
        self.board = Board()
        self.player = Player("X")
        self.computer = Player("O")
        
    def play(self):
        #using infinite loop to run the game
        while True:
            message = f"{self.player.name},Enter the position(1-9): "
            if self.player.type == "X":
                position = int(input(message))
            
                if self.board.update_board(position, self.player.type):
                    self.board.print_board()
                    

                        #Changing the player to computer
                self.player, self.computer = self.computer, self.player

            else:
                position = random.randint(1, 9)
                if self.board.update_board(position, self.player.type):
                    self.board.print_board()
                    
                
                        #Changing the player to user
                self.player, self.computer = self.computer, self.player
                    

game = Game()
game.play()