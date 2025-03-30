from simulation import Simulation
from agent_factory import AgentFactory

def get_position(prompt, world_size):
    while True:
        try:
            pos = input(f"{prompt} (format: x,y): ").strip()
            x, y = map(int, pos.split(','))
            if 0 <= x < world_size and 0 <= y < world_size:
                return (x, y)
            else:
                print("❌ Out of bounds.")
        except:
            print("❌ Invalid format. Use x,y (e.g. 1,3)")

def get_obstacles(world_size, agent_start, goal_pos):
    obstacles = []
    print("Enter obstacle positions (x,y). Type 'done' when finished.")
    while True:
        inp = input("Obstacle: ").strip()
        if inp.lower() == 'done':
            break
        try:
            x, y = map(int, inp.split(','))
            pos = (x, y)
            if pos in [agent_start, goal_pos]:
                print("❌ Cannot place on agent or goal.")
            elif 0 <= x < world_size and 0 <= y < world_size:
                obstacles.append(pos)
            else:
                print("❌ Out of bounds.")
        except:
            print("❌ Invalid format. Use x,y")
    return obstacles


def main():
    print("👋 Welcome to Custom GridWorld Setup")

    world_size = int(input("Enter grid size (e.g. 10 for 10x10): "))
    agent_start = get_position("Enter agent start position", world_size)
    goal_pos = get_position("Enter goal position", world_size)
    obstacles = get_obstacles(world_size, agent_start, goal_pos)

    available_agents = AgentFactory.get_available_agents()
    print("\nAvailable agents:", ", ".join(available_agents))
    agent_choice = input("Select an agent type: ").strip().lower()
    while agent_choice not in available_agents:
        print("❌ Invalid choice.")
        agent_choice = input("Select an agent type: ").strip().lower()

    sim = Simulation(
        world_size=world_size,
        agent_start=agent_start,
        goal_pos=goal_pos,
        obstacles=obstacles,
        max_steps=100
    )

    sim.agent = AgentFactory.get_agent(agent_choice, agent_start, sim.world)
    sim.run(visualize=True)


if __name__ == "__main__":
    main()
