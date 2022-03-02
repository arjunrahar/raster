import pickle as pkl
import numpy as np
RT = 'cam_sampled_RTs.pkl'
data = pkl.load(open(RT, 'rb'))

print(type(data))
print(len(data))
print(data[5000])
