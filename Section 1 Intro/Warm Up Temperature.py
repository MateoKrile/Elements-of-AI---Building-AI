import random
import numpy as np

def accept_prob(S_old, S_new, T):
    return min(np.exp(-(S_old-S_new)/T), 1)

def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)