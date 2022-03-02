#!/usr/bin/env python3
import pickle as pkl
import numpy as np
from PIL import Image
from pathlib import Path
RT = 'ape_info.pkl'
data = pkl.load(open(RT, 'rb'))

#print(type(data))
#print(len(data))
#print(data[10])
print(data[0])
print("len", len(data))
#na = data['rgb']
cls = RT
new = RT.replace('.pkl', '')
#cls = str(RT) - str('.pkl')
print(new)
#msk = np.array([[1,2,3,4],[2,3,4,5]],[[1,2,3,4],[2,3,4,5]])
msk = np.arange(30).reshape(2, 3, 5)
print("shape", msk.shape)
print("msk",msk)
msk = np.sum(msk,0)>0
msk = np.asarray(msk,np.int32)
print("sum",msk)
hs, ws = np.nonzero(msk)
print(hs, ws)
#Image.fromarray(na).save("{}.png").format()
