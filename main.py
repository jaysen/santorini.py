# main.py
from player import Player
from game import Game

if __name__ == "__main__":
    player1 = Player("Player 1", "A1", "A2")
    player2 = Player("Player 2", "B1", "B2")
    game = Game(player1, player2)
    game.start_game()
