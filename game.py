# game.py
from board import Board
from player import Player

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = {player1.name: player1, player2.name: player2}
        self.current_player = player1
        self.init_workers()

    def init_workers(self):
        for player in self.players.values():
            for worker in player.workers:
                while True:
                    try:
                        row, col = map(int, input(f"{player.name}, enter starting position for {worker} (row col): ").split())
                        self.board.place_worker(worker, row, col)
                        break
                    except ValueError as e:
                        print(f"Invalid input: {e}. Try again.")
        self.board.display()

    def switch_turn(self):
        self.current_player = list(self.players.values())[1] if self.current_player == list(self.players.values())[0] else list(self.players.values())[0]

    def play_turn(self):
        print(f"{self.current_player.name}'s turn")
        self.board.display()
        while True:
            try:
                worker_id = input(f"Choose worker ({self.current_player.workers[0]}/{self.current_player.workers[1]}): ")
                move_to = tuple(map(int, input("Enter move position (row col): ").split()))
                self.board.move_worker(worker_id, *move_to)
                if self.board.check_win(worker_id):
                    print(f"{self.current_player.name} wins!")
                    self.board.display()
                    return True
                build_at = tuple(map(int, input("Enter build position (row col): ").split()))
                self.board.build(*build_at)
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Try again.")
        self.switch_turn()
        return False

    def start_game(self):
        while True:
            if self.play_turn():
                break