import random
import numpy as np
from typing import Tuple
from agents.agent import Agent

class QLearningAgent(Agent):
    def __init__(self, start_position: Tuple[int, int], world, episodes=500, alpha=0.1, gamma=0.9, epsilon=0.1):
        super().__init__(start_position, world)
        self.alpha = alpha              # Learning rate
        self.gamma = gamma              # Discount factor
        self.epsilon = epsilon          # Exploration rate
        self.episodes = episodes        # Number of training episodes
        self.q_table = {}               # Q-table: {(state): [action_values]}
        self.actions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right
        self.train()

    def get_state(self, position):
        return position

    def get_valid_actions(self, position):
        valid = []
        for i, (dx, dy) in enumerate(self.actions):
            new_pos = (position[0] + dx, position[1] + dy)
            if self.world.is_valid_position(new_pos):
                valid.append((i, new_pos))
        return valid

    def choose_action(self, state):
        if random.random() < self.epsilon or state not in self.q_table:
            return random.choice(self.get_valid_actions(state))[0]  # explore
        return np.argmax(self.q_table[state])  # exploit

    def train(self):
        for ep in range(self.episodes):
            state = self.world.start  # always starts from the same position
            self.position = state
            done = False

            while not done:
                state_key = self.get_state(state)
                if state_key not in self.q_table:
                    self.q_table[state_key] = np.zeros(len(self.actions))

                action_idx = self.choose_action(state_key)
                dx, dy = self.actions[action_idx]
                next_state = (state[0] + dx, state[1] + dy)

                if not self.world.is_valid_position(next_state):
                    reward = -1
                    next_state = state
                elif self.world.grid[next_state] == 2:
                    reward = 10
                    done = True
                else:
                    reward = -0.1

                next_state_key = self.get_state(next_state)
                if next_state_key not in self.q_table:
                    self.q_table[next_state_key] = np.zeros(len(self.actions))

                # Q-learning update
                old_value = self.q_table[state_key][action_idx]
                next_max = np.max(self.q_table[next_state_key])
                new_value = old_value + self.alpha * (reward + self.gamma * next_max - old_value)
                self.q_table[state_key][action_idx] = new_value

                state = next_state

    def move(self):
        state_key = self.get_state(self.position)
        if state_key in self.q_table:
            best_action = np.argmax(self.q_table[state_key])
            dx, dy = self.actions[best_action]
            next_pos = (self.position[0] + dx, self.position[1] + dy)
            if self.world.is_valid_position(next_pos):
                self.position = next_pos
