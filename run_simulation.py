import torch
from stable_baselines3 import PPO
from envs.attack_env import AdversaryEnv

# Load trained AI model
model = PPO.load("models/ai_attack_model")

# Initialize attack environment
env = AdversaryEnv()
obs = env.reset()

done = False
while not done:
    action, _ = model.predict(obs)
    obs, reward, done, _ = env.step(action)
    env.render()
