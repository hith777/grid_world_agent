import numpy as np
from typing import List, Tuple

EMPTY, GOAL, OBSTACLE = 0, 2, -1

class GridWorld:
    def __init__(self, size: int):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)

    def place_goal(self, position: Tuple[int, int]):
        self.grid[position] = GOAL

    def place_obstacles(self, obstacles: List[Tuple[int, int]]):
        for pos in obstacles:
            self.grid[pos] = OBSTACLE

    def is_valid_position(self, position: Tuple[int, int]) -> bool:
        x, y = position
        return (0 <= x < self.size and
                0 <= y < self.size and
                self.grid[position] != OBSTACLE)

    def display(self, agent_position: Tuple[int, int]):
        symbols = {EMPTY: ".", GOAL: "G", OBSTACLE: "X"}
        for i in range(self.size):
            row = ""
            for j in range(self.size):
                if (i, j) == agent_position:
                    row += "A "
                else:
                    row += f"{symbols[self.grid[i,j]]} "
            print(row)
        print()
