import random
import math

class Bandit:
    
    def __init__(self, arms=10):
        self.occurrences = [0] * arms
        self.cumulative_rewards = [0] * arms
        self.arms = [random.randint(1, arms) for i in range (0, arms)]
        self.episodes = 1000
        self.reward = [[0 for i in range (0, len(self.arms))] for j in range(0, self.episodes)]

    def choose_arm(self, step):
        alpha = 0.1
        sum = 0

        for i in range(0, len(self.arms)):
            self.reward[step-1][i] = math.sin((i + 1) * (step + 1)) * self.arms[i]
        
        
        for k in range(0, len(self.arms)):
            for j in range (0, step):
                sum = sum + alpha * (1-alpha)**(step-(j+1)) * self.reward[j][k]

            self.cumulative_rewards[k] =  (1-alpha)**(k+1) * self.arms[k] + sum
            sum = 0
        
        return self.cumulative_rewards.index(max(self.cumulative_rewards))
     
    def run(self):
        bandit = Bandit()
        expected_reward = [0] * self.episodes

        for i in range(0, self.episodes):
            expected_reward[i] = bandit.choose_arm(i+1)
        return expected_reward

bandit = Bandit()
bandit.run()