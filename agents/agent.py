from typing import Tuple
from gridworld import GridWorld

class Agent:
    def __init__(self, start_position: Tuple[int, int], world: GridWorld):
        self.position = start_position
        self.world = world

    def move(self):
        raise NotImplementedError("This method should be overridden.")

    def reached_goal(self) -> bool:
        return self.world.grid[self.position] == 2
