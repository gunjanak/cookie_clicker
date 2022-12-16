import numpy as np
import math

Q = np.zeros((10, 3))

Q[1,2] = 5
print(Q)
tok = 5.3
tic = 2.6
print("current time is %d" %math.floor(tok-tic))
rewards = np.zeros(10)
rewards[2] = 5
print(rewards)
print(Q[1].max())
Q[1] = [10,1,0]
print(Q)