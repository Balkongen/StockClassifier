import pandas as pd
import numpy as np
from prepare_data import prepare_data


class RL:

    def __init__(self, data: pd.DataFrame, Q = None) -> None:
        self.data = data
        self.Q = Q


    def get_reward(date: str) -> int:
        # return profit/loss as reward?
        return None
    
    
    def is_terminal_state(date, lastDate) -> bool:

        return date == lastDate


    def get_next_action(self, current_state: int, epsilon: float) -> int:
        # TODO Prevent illegal action
        if np.random.random() > epsilon:
            return np.argmax(self.Q[current_state])  # Exploit best-known action
        else:
            return np.random.randint(self.Q.shape[1])  # Explore with random action
        

def run(number_of_episodes, epsilone = 0, discount_factor = 0.2, learning_rate = 0.9):
    data = prepare_data(5, 20, 50, 0.014)
    data = data.iloc[4500:] # Remove some data
    
    last_date = data["Date"].tail(1)

    actions = ["buy", "hold", "sell"]
    env = RL(data=data)

    total_profit = 0
    number_of_trades = 0

    for episode in range(number_of_episodes):

        current_date = data["Date"].head(1)
        while not env.is_terminal_state(current_date, last_date):
            
            
            return


    
    return None


if __name__ == "__main__":
    run(10)