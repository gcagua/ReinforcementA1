import random

class Bandit:
    
    def __init__(self, arms=10):
        self.reward = [0] * arms # es cero o es la recompensa inicial?
        self.occurrences = [0] * arms
        self.cumulative_rewards = [0] * arms
        self.arms = [random.uniform(-3,3) for i in range (0, arms)]
        self.reward = self.arms

    def choose_arm(self):
        epsilon = 0.01
        # seleccionar el máximo
        aleatorio = random.random()
        # añadir posición de ocurrencias y recompensas
        if aleatorio > epsilon:
            # no cambia de brazo y se mantiene con el de valor esperado más alto
            arm = self.reward.index(max(self.reward))
        else: 
            arm = random.randint(0, len(self.arms)-1)

        self.occurrences[arm] = self.occurrences[arm] + 1
        self.reward[arm] = self.reward[arm] + (1 / self.occurrences[arm]) * (self.arms[arm] - self.reward[arm])
        return self.reward[arm]
     
    def run(self):
        episodes = 1000
        bandit = Bandit()
        expected_reward = [0] * episodes
        for i in range(0, episodes):
            expected_reward[i] = bandit.choose_arm()
        return expected_reward

bandit = Bandit()
bandit.run()