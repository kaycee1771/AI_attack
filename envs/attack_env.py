import gym
import numpy as np
from gym import spaces

class AdversaryEnv(gym.Env):
    def __init__(self):
        super(AdversaryEnv, self).__init__()

        # Define state space (e.g., IAM roles, open ports, access level)
        self.state = np.array([0, 0, 0])  # [Privilege Level, Detection Risk, Persistence]
        
        # Define action space (attack options)
        self.action_space = spaces.Discrete(4)  # 4 attack moves
        
        # Define observation space
        self.observation_space = spaces.Box(low=0, high=10, shape=(3,), dtype=np.float32)

    def step(self, action):
        reward = 0
        done = False

        # Define attack moves
        if action == 0:  # Privilege Escalation
            self.state[0] += 2
            reward += 10
        elif action == 1:  # Credential Theft
            self.state[2] += 1
            reward += 5
        elif action == 2:  # Lateral Movement
            self.state[0] += 1
            self.state[1] += 2  # Detection risk increases
            reward += 7
        elif action == 3:  # Persistence (Backdoor)
            self.state[2] += 3
            reward += 8

        # Apply penalties
        if self.state[1] > 5:  # Detection risk threshold
            reward -= 15
            done = True

        return self.state, reward, done, {}

    def reset(self):
        self.state = np.array([0, 0, 0])  # Reset environment
        return self.state

    def render(self):
        print(f"State: Privilege={self.state[0]}, Detection={self.state[1]}, Persistence={self.state[2]}")
