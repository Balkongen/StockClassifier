import pandas as pd
import numpy as np


class RL:

    def __init__(self, data: pd.Dataframe, Q = None) -> None:
        self.data = data
        self.Q = Q


    def get_reward(date: str) -> int:
        # return profit/loss as reward?
        return None
    

    def get_next_action(self, current_state: int, epsilon: float) -> int:
        
        if np.random.random() > epsilon:
            return np.argmax(self.Q[current_state])  # Exploit best-known action
        else:
            return np.random.randint(self.Q.shape[1])  # Explore with random action
