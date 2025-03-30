from agents.random_agent import RandomAgent
from agents.bfs_agent import BFSAgent
from agents.astar_agent import AStarAgent
from agents.q_learning_agent import QLearningAgent

class AgentFactory:
    _agents = {
        "random": RandomAgent,
        "bfs": BFSAgent,
        "astar": AStarAgent,
        "qlearning": QLearningAgent,
    }

    @classmethod
    def get_agent(cls, agent_type, start_pos, world):
        agent_cls = cls._agents.get(agent_type.lower())
        if agent_cls is None:
            raise ValueError(f"Agent type '{agent_type}' not found.")
        return agent_cls(start_pos, world)

    @classmethod
    def get_available_agents(cls):
        return list(cls._agents.keys())
