import gym
import torch
from stable_baselines3 import PPO
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from envs.attack_env import AdversaryEnv

# Load the attack simulation environment
env = AdversaryEnv()

# Train using PPO (Proximal Policy Optimization)
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=50000)

# Save the trained model
model.save("models/ai_attack_model")
print("AI Training Complete & Model Saved!")
