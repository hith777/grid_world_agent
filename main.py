from simulation import Simulation

def main():
    world_size = 10  # Dynamic grid size
    agent_start = (0, 0)
    goal_pos = (9, 9)
    obstacles = [(1,2), (2,2), (3,1), (4,4), (5,6), (7,3)]  # Customizable obstacles

    sim = Simulation(
        world_size=world_size,
        agent_start=agent_start,
        goal_pos=goal_pos,
        obstacles=obstacles,
        max_steps=100
    )

    sim.run()

if __name__ == "__main__":
    main()
