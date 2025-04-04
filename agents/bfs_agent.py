from collections import deque
from typing import List, Tuple, Optional
from agents.agent import Agent

class BFSAgent(Agent):
    def __init__(self, start_position: Tuple[int, int], world):
        super().__init__(start_position, world)
        self.path = self.find_path_to_goal()

    def find_path_to_goal(self) -> Optional[List[Tuple[int, int]]]:
        visited = set()
        queue = deque([[self.position]])

        while queue:
            path = queue.popleft()
            current = path[-1]

            if self.world.grid[current] == 2:  # Check if current cell is the Goal
                return path[1:]  # return path excluding starting position

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])

        return None  # If no path is found

    def get_neighbors(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for dx, dy in directions:
            new_pos = (position[0] + dx, position[1] + dy)
            if self.world.is_valid_position(new_pos):
                moves.append(new_pos)
        return moves

    def move(self):
        if self.path:
            self.position = self.path.pop(0)
