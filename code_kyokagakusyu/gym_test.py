import gym
import time
import pandas as pd

env = gym.make("FrozenLake-v1")
env.reset()


class Planner:
    def __init__(self,env) -> None:
        self.env = env
    
    def s_to_loc(self,s):
        row = s//self.env.ncol
        col  =s%self.env.ncol
        return row,col
    
    def rewards(self,s):
        row,col = self.s_to_loc(s)
        if self.env.desc[row][col]== b"H":
            return -1
        elif self.env.desc[row][col]== b"G":
            return 1
        else:
            return 0
    
    def plan(self,ganmma=0.9,threshhold=0.0001):
        self.env.reset()
        v = {}
        for s in range(self.env.nS):
            v[s] = self.reward(s)
        while True:
            delta = 0
            for s in v:
                row,col = self.s_to_loc(s)
                if self.env.desc[row][col] in [b"H",b"G"]:
                    continue
                expected_rewards = []
                for a in range(self.env.nA):
                    for prob,next_s,_,_ in self.env.P[s][a]:
                        r += ganmma * prob * v[next_s]
                    expected_rewards.append(r)
                max_rewards = max(expected_rewards)
                new_V = self.rewards(s)+max_rewards
                reward = self.rewards(s)+max_rewards

                #|v_i+1-v_i|
                delta = max(delta,abs(reward-v[s]))
                v[s] = new_V

            if delta<threshhold:
                break 
        return self.dict_to_grid(V)
    def dict_to_grid(self,V):
        grid = []
        for i in range(self.env.nrow):
            row = [0] * self.env.ncol
            grid.append(row)
        for s in V:
            row,col = self.s_to_loc(s)
            grid[row][col] = V(s)
        return pd.DataFrame(grid)

env.render()

print(env.desc)
time.sleep(100)