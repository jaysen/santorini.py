# board.py
class Board:
    def __init__(self):
        self.grid = [[0 for _ in range(5)] for _ in range(5)]  # 5x5 grid with levels 0-4
        self.workers = {}  # Maps worker IDs to positions (row, col)

    def display(self):
        print("  0 1 2 3 4")
        print(" +-----------+")
        for row in range(5):
            print(f"{row}|", end=' ')
            for col in range(5):
                worker_symbol = None
                for worker, pos in self.workers.items():
                    if pos == (row, col):
                        worker_symbol = worker
                        break
                if worker_symbol:
                    print(worker_symbol, end=' ')
                else:
                    print(self.grid[row][col], end=' ')
            print("|")
        print(" +-----------+")

    def place_worker(self, worker_id, row, col):
        if (row, col) not in self.workers.values():
            self.workers[worker_id] = (row, col)
        else:
            raise ValueError("Position already occupied by another worker")

    def move_worker(self, worker_id, new_row, new_col):
        if worker_id not in self.workers:
            raise ValueError("Worker does not exist")
        old_row, old_col = self.workers[worker_id]
        if self.is_valid_move(old_row, old_col, new_row, new_col):
            self.workers[worker_id] = (new_row, new_col)
        else:
            raise ValueError("Invalid move")

    def build(self, row, col):
        if self.grid[row][col] < 4:
            self.grid[row][col] += 1
        else:
            raise ValueError("Cannot build beyond level 4")

    def is_valid_move(self, old_row, old_col, new_row, new_col):
        if not (0 <= new_row < 5 and 0 <= new_col < 5):
            return False  # Out of bounds
        if (new_row, new_col) in self.workers.values():
            return False  # Occupied by another worker
        height_diff = self.grid[new_row][new_col] - self.grid[old_row][old_col]
        if height_diff > 1:
            return False  # Cannot move up more than one level
        return True

    def check_win(self, worker_id):
        row, col = self.workers[worker_id]
        return self.grid[row][col] == 3  # Win condition: standing on level 3