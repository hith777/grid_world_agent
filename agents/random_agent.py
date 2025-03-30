import random
from agents.agent import Agent

class RandomAgent(Agent):
    def get_possible_moves(self):
        moves = []
        x, y = self.position
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for dx, dy in directions:
            new_pos = (x+dx, y+dy)
            if self.world.is_valid_position(new_pos):
                moves.append(new_pos)
        return moves

    def move(self):
        moves = self.get_possible_moves()
        if moves:
            self.position = random.choice(moves)
