from gridworld import GridWorld
from typing import Tuple, List
import time
from visualizer import Visualizer


class Simulation:
    def __init__(self, world_size: int, agent_start: Tuple[int,int], goal_pos: Tuple[int,int], obstacles: List[Tuple[int,int]], max_steps: int = 100):
        self.world = GridWorld(world_size)
        self.world.setup_grid(agent_start, goal_pos, obstacles)  # ← Must be called before agent
        self.agent = None  # set later in main
        self.max_steps = max_steps

    def run(self, visualize=False):
        steps = 0
        if visualize:
            viz = Visualizer(self.world.size)
            viz.render(self.world.grid, self.agent.position)

        while not self.agent.reached_goal() and steps < self.max_steps:
            self.agent.move()
            steps += 1

            if visualize:
                viz.render(self.world.grid, self.agent.position)
            else:
                print(f"Step {steps}:")
                self.world.display(self.agent.position)

        if visualize:
            time.sleep(1)
            viz.close()

        if self.agent.reached_goal():
            print(f"Goal reached in {steps} steps! 🎉")
        else:
            print("Max steps reached. Goal not reached.")

