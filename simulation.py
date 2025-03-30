from grid_world_agent.agents.agent import Agent
from gridworld import GridWorld
from typing import Tuple, List

class Simulation:
    def __init__(self, world_size: int, agent_start: Tuple[int,int], goal_pos: Tuple[int,int], obstacles: List[Tuple[int,int]], max_steps: int = 100):
        self.world = GridWorld(world_size)
        self.world.place_goal(goal_pos)
        self.world.place_obstacles(obstacles)
        self.agent = Agent(agent_start, self.world)
        self.max_steps = max_steps

    def run(self):
        steps = 0
        print("Initial State:")
        self.world.display(self.agent.position)

        while not self.agent.reached_goal() and steps < self.max_steps:
            self.agent.move()
            steps += 1
            print(f"Step {steps}:")
            self.world.display(self.agent.position)

        if self.agent.reached_goal():
            print(f"Goal reached in {steps} steps! 🎉")
        else:
            print("Goal not reached within step limit.")
