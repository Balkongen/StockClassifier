import pandas as pd
import numpy as np
from prepare_data import prepare_data


class RL:

    def __init__(self, data: pd.DataFrame, Q = None) -> None:
        self.data = data
        self.Q = Q


    def get_reward(self, date, action) -> int:
        # return profit/loss as reward?
        # return reward direct or during iteration?
        return None
    
    
    def is_terminal_state(self, date, last_date) -> bool:
        return date == last_date


    def get_next_action(self, current_state: int, epsilon: float) -> int:
        # TODO Prevent illegal action
        if np.random.random() > epsilon:
            return np.argmax(self.Q[current_state])  # Exploit best-known action
        else:
            return np.random.randint(self.Q.shape[1])  # Explore with random action
        

def run(number_of_episodes, epsilone = 0, discount_factor = 0.2, learning_rate = 0.9):
    data = prepare_data(5, 20, 50, 0.014)
    data = data.iloc[4500:] # Remove some data
    
    last_date = data["Date"].tail(1).values

    actions = ["buy", "hold", "sell"]
    env = RL(data=data)

    profit_arr = []
    
    for episode in range(number_of_episodes):
        
        total_profit = 0
        number_of_trades = 0
        day_count = 0
       
        current_day = data.iloc[day_count]
        current_date = current_day["Date"]
       
        
        while not env.is_terminal_state(current_date, last_date):
            print(current_date)
            
            
            action = env.get_next_action(None, epsilone) # FIXME Set proper state
            reward = env.get_reward(current_date, action)
            
            
            # DO something before
            day_count += 1
            current_day = data.iloc[day_count]
            current_date = current_day["Date"]
            
        profit_arr.append(total_profit)

    return None


if __name__ == "__main__":
    run(10)