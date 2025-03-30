import heapq
from typing import List, Tuple, Optional
from agents.agent import Agent

class AStarAgent(Agent):
    def __init__(self, start_position: Tuple[int, int], world):
        super().__init__(start_position, world)
        self.path = self.find_path_to_goal()

    def heuristic(self, pos: Tuple[int, int], goal: Tuple[int, int]) -> int:
        # Manhattan distance as heuristic
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

    def find_path_to_goal(self) -> Optional[List[Tuple[int, int]]]:
        start = self.position
        goal = tuple(zip(*((self.world.grid == 2).nonzero())))[0]

        open_set = []
        heapq.heappush(open_set, (0 + self.heuristic(start, goal), 0, [start]))

        visited = set()

        while open_set:
            estimated_cost, cost_so_far, path = heapq.heappop(open_set)
            current = path[-1]

            if current == goal:
                return path[1:]

            if current in visited:
                continue

            visited.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    new_cost = cost_so_far + 1
                    new_estimated_cost = new_cost + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (new_estimated_cost, new_cost, path + [neighbor]))

        return None  # No path found

    def get_neighbors(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            new_pos = (position[0] + dx, position[1] + dy)
            if self.world.is_valid_position(new_pos):
                moves.append(new_pos)
        return moves

    def move(self):
        if self.path:
            self.position = self.path.pop(0)
