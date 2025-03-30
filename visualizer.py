import matplotlib.pyplot as plt
import numpy as np

EMPTY, AGENT, GOAL, OBSTACLE = 0, 1, 2, -1

class Visualizer:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.fig, self.ax = plt.subplots()

    def render(self, grid, agent_position):
        visual_grid = np.copy(grid)
        x, y = agent_position
        visual_grid[x, y] = AGENT

        color_map = {
            EMPTY: 'white',
            OBSTACLE: 'black',
            GOAL: 'green',
            AGENT: 'blue',
        }

        self.ax.clear()
        self.ax.set_xticks(np.arange(-0.5, self.grid_size, 1), minor=True)
        self.ax.set_yticks(np.arange(-0.5, self.grid_size, 1), minor=True)
        self.ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5)

        for x in range(self.grid_size):
            for y in range(self.grid_size):
                val = visual_grid[x, y]
                self.ax.add_patch(plt.Rectangle((y, self.grid_size - x - 1), 1, 1,
                                   facecolor=color_map[val], edgecolor='gray'))

        self.ax.set_xlim(0, self.grid_size)
        self.ax.set_ylim(0, self.grid_size)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        plt.pause(0.2)

    def close(self):
        plt.close()
