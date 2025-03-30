from agents.random_agent import RandomAgent
from agents.bfs_agent import BFSAgent

class AgentFactory:
    @staticmethod
    def get_agent(agent_type, start_pos, world):
        agents = {
            "random": RandomAgent,
            "bfs": BFSAgent,
            # Future: "astar": AStarAgent, "qlearning": QLearningAgent, etc.
        }

        agent_cls = agents.get(agent_type.lower())
        if agent_cls is None:
            raise ValueError(f"Agent type '{agent_type}' not found.")
        return agent_cls(start_pos, world)
