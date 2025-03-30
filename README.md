# 🧠 GridWorld AI Agent Project

Welcome to **GridWorld AI Agent**, a Python-based environment where intelligent agents learn to navigate a grid with obstacles using classical and reinforcement learning methods. This project is designed with **SOLID principles**, full **CLI and GUI editors**, and modular architecture to scale easily.

---

## 📦 Features

- 🔁 Dynamic Grid size
- 🧱 Obstacle placement
- 🟦 Agent start & 🟩 Goal configuration
- 🤖 Multiple agent strategies: Random, BFS, A*, Q-Learning, Deep Q-Learning
- 🖱 GUI editor for board creation
- 🧠 Reinforcement learning support
- 📈 Visualizer (matplotlib) with path animation
- 💾 Model saving/loading (DQN)
- 📊 Reward plotting after training

---

## 🏛️ Architecture Diagram

```
+-----------------------------------------------------------------------------------+
|                              GridWorld AI Agent Project                           |
+-----------------------------------------------------------------------------------+
                                           │
                                           │
                                           ▼
                            ┌─────────────────────────────────┐
                            │         launcher.py             │ ◀── Hybrid CLI/GUI launcher
                            └─────────────────────────────────┘
                                │                       │
               ┌───────────────────────────┐      ┌────────────────────────────┐
               ▼                           ▼      ▼                            ▼
     ┌─────────────────────┐     ┌─────────────────────────┐        ┌────────────────────┐
     │  console_editor.py  │     │     grid_editor.py      │        │    visualizer.py    │
     │ (CLI Simulation)    │     │ (Tkinter GUI Editor)    │        │  (matplotlib grid)  │
     └─────────────────────┘     └─────────────────────────┘        └────────────────────┘
               │                           │
               ▼                           ▼
       ┌──────────────────────────────────────────────┐
       │                  Simulation                  │
       │        (Manages agent-world interaction)     │
       └──────────────────────────────────────────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
 ┌──────────────┐    ┌────────────────┐    ┌──────────────────┐
 │   GridWorld  │    │     Agent      │    │  AgentFactory     │
 │ (environment │    │ (Base logic)  │    │ (creates agents) │
 └──────────────┘    └────────────────┘    └──────────────────┘
                            │
    ┌──────────────────────────────────────────────────────────┐
    │                   agents/ (strategy module)              │
    │ ┌────────────────────┬────────────────────────────────┐ │
    │ │ random_agent.py    │  bfs_agent.py, astar_agent.py  │ │
    │ │ q_learning_agent.py│  dqn_agent.py (Deep RL)         │ │
    │ └────────────────────┴────────────────────────────────┘ │
    └──────────────────────────────────────────────────────────┘
```

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install numpy matplotlib torch
```

### 2. Launch Project

**Hybrid Launcher**:
```bash
python launcher.py
```
You’ll be prompted to pick:
- Console editor (type coordinates)
- GUI editor (click to place agent, goal, obstacles)

---

## 🎮 Controls in GUI Editor (`grid_editor.py`)

| Action        | Input                        |
|---------------|------------------------------|
| Add obstacle  | Left-click                   |
| Set Start     | Ctrl + Left-click            |
| Set Goal      | Shift + Left-click           |
| Run sim       | Click "Run Simulation" button|

---

## 🧠 Available Agents

| Name      | Description                             |
|-----------|-----------------------------------------|
| `random`  | Moves randomly                          |
| `bfs`     | Breadth-first search (shortest path)    |
| `astar`   | A* search with heuristic                |
| `qlearning`| Table-based Q-learning RL              |
| `deepq`   | Deep Q-Network (Neural Net RL)          |

---

## 💾 Saving and Loading Models

- Deep Q-Network auto-saves to `dqn_model.pth`
- If model is detected, you’ll be asked whether to load it or retrain

---

## 📈 Reward Plot (DQN)

After training with `deepq`, you’ll see a matplotlib chart showing episode rewards over time.

---

## 🧪 Future Ideas

- 🎮 Live game mode to control agent manually
- 💾 Save/load grid layout to JSON
- 📊 Web-based stats dashboard
- 🧠 Add PPO/DQN with target networks

---

## 📂 Project Structure

```
gridworld_agent/
├── agents/
│   ├── agent.py
│   ├── random_agent.py
│   ├── bfs_agent.py
│   ├── astar_agent.py
│   ├── q_learning_agent.py
│   └── dqn_agent.py
├── visualizer.py
├── gridworld.py
├── simulation.py
├── agent_factory.py
├── console_editor.py
├── grid_editor.py
├── launcher.py
└── README.md
```

---