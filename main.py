from simulation import Simulation
from agent_factory import AgentFactory

def main():
    world_size = 10
    agent_start = (0, 0)
    goal_pos = (9, 9)
    obstacles = [(1,2), (2,2), (3,1), (4,4), (5,6), (7,3)]

    available_agents = AgentFactory.get_available_agents()
    print("Available agents:", ", ".join(available_agents))

    agent_choice = input("Select an agent type: ").strip().lower()

    while agent_choice not in available_agents:
        print("Invalid choice, please select from:", ", ".join(available_agents))
        agent_choice = input("Select an agent type: ").strip().lower()

    sim = Simulation(
        world_size=world_size,
        agent_start=agent_start,
        goal_pos=goal_pos,
        obstacles=obstacles,
        max_steps=50
    )

    sim.agent = AgentFactory.get_agent(agent_choice, agent_start, sim.world)
    sim.run()

if __name__ == "__main__":
    main()
