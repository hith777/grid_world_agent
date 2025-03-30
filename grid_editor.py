import tkinter as tk
from tkinter import messagebox
from agent_factory import AgentFactory
from simulation import Simulation

CELL_SIZE = 40
DEFAULT_SIZE = 10

EMPTY, OBSTACLE, START, GOAL = 0, -1, 1, 2

class GridEditor:
    def __init__(self, master, grid_size=DEFAULT_SIZE):
        self.master = master
        self.grid_size = grid_size
        self.canvas = tk.Canvas(master, width=grid_size*CELL_SIZE, height=grid_size*CELL_SIZE, bg='white')
        self.canvas.pack()

        self.grid = [[EMPTY for _ in range(grid_size)] for _ in range(grid_size)]
        self.start = None
        self.goal = None

        self.canvas.bind("<Button-1>", self.left_click)              # normal left click
        self.canvas.bind("<Shift-Button-1>", self.shift_click)       # shift + left click
        self.canvas.bind("<Control-Button-1>", self.ctrl_click)      # ctrl + left click


        self.agent_var = tk.StringVar(master)
        self.agent_var.set(AgentFactory.get_available_agents()[0])
        agent_menu = tk.OptionMenu(master, self.agent_var, *AgentFactory.get_available_agents())
        agent_menu.pack()

        start_button = tk.Button(master, text="Run Simulation", command=self.run_simulation)
        start_button.pack()

        self.draw_grid()

    def draw_grid(self):
        self.canvas.delete("all")
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                x0, y0 = j * CELL_SIZE, i * CELL_SIZE
                x1, y1 = x0 + CELL_SIZE, y0 + CELL_SIZE
                color = "white"
                if self.grid[i][j] == OBSTACLE:
                    color = "black"
                elif (i, j) == self.start:
                    color = "blue"
                elif (i, j) == self.goal:
                    color = "green"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="gray")

    def left_click(self, event):
        i, j = event.y // CELL_SIZE, event.x // CELL_SIZE
        if (i, j) != self.start and (i, j) != self.goal:
            self.grid[i][j] = OBSTACLE if self.grid[i][j] == EMPTY else EMPTY
        self.draw_grid()

    def ctrl_click(self, event):
        i, j = event.y // CELL_SIZE, event.x // CELL_SIZE
        if self.goal == (i, j): return
        self.start = (i, j)
        self.draw_grid()


    def shift_click(self, event):
        i, j = event.y // CELL_SIZE, event.x // CELL_SIZE
        if self.start == (i, j): return
        self.goal = (i, j)
        self.draw_grid()

    def run_simulation(self):
        if not self.start or not self.goal:
            messagebox.showerror("Error", "Start and Goal must be set.")
            return

        obstacles = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size)
                     if self.grid[i][j] == OBSTACLE]

        sim = Simulation(
            world_size=self.grid_size,
            agent_start=self.start,
            goal_pos=self.goal,
            obstacles=obstacles,
            max_steps=100
        )

        agent_choice = self.agent_var.get()
        sim.agent = AgentFactory.get_agent(agent_choice, self.start, sim.world)
        sim.run(visualize=True)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("GridWorld Board Editor")
    app = GridEditor(root)
    root.mainloop()
