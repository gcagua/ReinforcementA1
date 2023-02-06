import random

class Bandit:
    
    def __init__(self, arms=10):
        self.occurrences = [0] * arms
        self.cumulative_rewards = [0] * arms
        self.arms = [random.uniform(-3,3) for i in range (0, arms)]

    def choose_arm(self):
        # seleccionar el máximo
        arm = self.arms.index(max(self.arms)) 
        # añadir posición de ocurrencias y recompensas
        self.occurrences[arm] = self.occurrences[arm] +1
        self.cumulative_rewards[arm] = self.cumulative_rewards[arm] + self.arms[arm]
        # retornar el Q para ese brazo
        return self.cumulative_rewards[arm]/self.occurrences[arm]
     
    def run(self):
        episodes = 1000
        bandit = Bandit()
        expected_reward = [0] * episodes
        for i in range(0, episodes):
            expected_reward[i] = bandit.choose_arm()
        return expected_reward

bandit = Bandit()
bandit.run()