import matplotlib.pyplot as plt
import numpy as np
import random
import torch
import torch.nn as nn
import torch.optim as optim
from collections import deque
from agents.agent import Agent
import os

EMPTY, AGENT, GOAL, OBSTACLE = 0, 1, 2, -1

# DQN Hyperparameters
EPISODES = 100
LR = 0.001
GAMMA = 0.95
EPSILON = 1.0
EPSILON_DECAY = 0.995
EPSILON_MIN = 0.1
BATCH_SIZE = 32
MEMORY_SIZE = 1000
MODEL_PATH = "dqn_model.pth"

class DQNetwork(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(DQNetwork, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, output_dim)
        )

    def forward(self, x):
        return self.fc(x)

class DQNAgent(Agent):
    def __init__(self, start_pos, world):
        super().__init__(start_pos, world)
        self.state_size = 2
        self.action_size = 4
        self.model = DQNetwork(self.state_size, self.action_size)
        self.optimizer = optim.Adam(self.model.parameters(), lr=LR)
        self.criterion = nn.MSELoss()

        self.epsilon = EPSILON
        self.memory = deque(maxlen=MEMORY_SIZE)
        self.actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.episode_rewards = []

        if os.path.exists(MODEL_PATH):
            print("\n[DQN] Pre-trained model detected.")
            print("[1] Train from scratch")
            print("[2] Load pre-trained model")
            choice = input("Enter 1 or 2: ").strip()

            while choice not in ["1", "2"]:
                print("❌ Invalid choice. Please enter 1 or 2.")
                choice = input("Enter 1 or 2: ").strip()

            if choice == "2":
                self.load_model()
            else:
                self.train_agent()
        else:
            print("\n[DQN] No pre-trained model found. Starting training...")
            self.train_agent()

    def get_state_tensor(self, pos):
        return torch.tensor(pos, dtype=torch.float32)

    def get_valid_actions(self, pos):
        return [(i, (pos[0] + dx, pos[1] + dy))
                for i, (dx, dy) in enumerate(self.actions)
                if self.world.is_valid_position((pos[0] + dx, pos[1] + dy))]

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.get_valid_actions(state))[0]
        with torch.no_grad():
            q_values = self.model(self.get_state_tensor(state))
            return torch.argmax(q_values).item()

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def replay(self):
        if len(self.memory) < BATCH_SIZE:
            return
        batch = random.sample(self.memory, BATCH_SIZE)
        for state, action, reward, next_state, done in batch:
            state_t = self.get_state_tensor(state)
            next_state_t = self.get_state_tensor(next_state)
            target = reward
            if not done:
                with torch.no_grad():
                    target += GAMMA * torch.max(self.model(next_state_t)).item()
            output = self.model(state_t)
            target_f = output.clone()
            target_f[action] = target
            loss = self.criterion(output, target_f.detach())
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

    def train_agent(self):
        for episode in range(EPISODES):
            total_reward = 0
            state = self.world.start
            self.position = state
            done = False

            while not done:
                action_idx = self.choose_action(state)
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

                self.remember(state, action_idx, reward, next_state, done)
                state = next_state
                total_reward += reward
                self.replay()

            self.episode_rewards.append(total_reward)
            print(f"Episode {episode+1}/{EPISODES} — Total reward: {total_reward:.2f} — Epsilon: {self.epsilon:.2f}")

            if self.epsilon > EPSILON_MIN:
                self.epsilon *= EPSILON_DECAY

        self.save_model()
        self.plot_rewards()

    def move(self):
        action_idx = self.choose_action(self.position)
        dx, dy = self.actions[action_idx]
        next_pos = (self.position[0] + dx, self.position[1] + dy)
        if self.world.is_valid_position(next_pos):
            self.position = next_pos

    def save_model(self):
        torch.save(self.model.state_dict(), MODEL_PATH)
        print(f"✅ Model saved to {MODEL_PATH}")

    def load_model(self):
        self.model.load_state_dict(torch.load(MODEL_PATH))
        self.model.eval()
        print(f"📥 Loaded model from {MODEL_PATH}")

    def plot_rewards(self):
        plt.plot(self.episode_rewards)
        plt.xlabel("Episode")
        plt.ylabel("Total Reward")
        plt.title("Training Performance (DQN)")
        plt.grid()
        plt.show()