import os
import time
import cv2
import pickle
import yaml
import numpy as np
import random
from random import randint
from random import shuffle
from glob import glob
from tqdm import tqdm
from PIL import ImageFile, Image
from plyfile import PlyData
from concurrent.futures import ProcessPoolExecutor
from argparse import ArgumentParser


lm_obj_dict={
    'ape':1,
    'benchvise':2,
    'cam':4,
    'can':5,
    'cat':6,
    'driller':8,
    'duck':9,
    'eggbox':10,
    'glue':11,
    'holepuncher':12,
    'iron':13,
    'lamp':14,
    'phone':15
}

root = './Linemod_preprocessed'
cls_root_ptn = os.path.join(root, "virtual_data/01/")

input_dir = os.path.join(root, "renders", "ape")

lst_pth = os.path.join(input_dir, "file_list.txt")

output_dir = os.path.join(root, "virtual_data")



def ensure_dir(pth):
    if not os.path.exists(pth):
        os.system("mkdir -p {}".format(pth))

def read_lines(pth):
    with open(pth, 'r') as f:
        return [
            line.strip() for line in f.readlines()
        ]

def collect_info(tr_pth):
    
    train_fns = read_lines(tr_pth)
    print(train_fns[0])
    print(type(train_fns[0]))
    return train_fns

def read_pickle(pkl_path):
    with open(pkl_path, 'rb') as f:
        return pickle.load(f)

train_fns = collect_info(lst_pth)

LA = len(train_fns)
random.shuffle(train_fns)
lst = train_fns[:20]
LA1 = len(lst)
#print(LA, type(LA))
pdata = {}
for idx in range(LA):
    
    pt = train_fns[idx]
    data = read_pickle(pt)

    rgb = data['rgb']
    depth= data['depth']
    mask = data['mask']
    RT = data['RT']
    rgb_pth = os.path.join(cls_root_ptn, "rgb")
    mask_pth = os.path.join(cls_root_ptn, "mask")
    depth_pth = os.path.join(cls_root_ptn, "depth")
    rgb = np.array(rgb)
    bgr = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)
    cv2.imwrite(os.path.join(rgb_pth,'%02d.png' %idx), bgr)
    depthMap = np.array(depth)
    cv2.imwrite(os.path.join(depth_pth,'%02d.png' %idx), depthMap)
    mask = np.array(mask)
    cv2.imwrite(os.path.join(mask_pth,'%02d.png' %idx), mask)

    a = idx
    plst_pth = os.path.join(cls_root_ptn, "gt.yml")
    ab = np.resize(np.array(RT[:, :3]), (1, 9))
    ac = np.resize(np.array(RT[:, 3]), (1, 3))*1000
    ab = ab.tolist()
    ac = ac.tolist()
    ab = ab[0]
    ac = ac[0]
    #data = {}
    pdata[idx]= {
            'cam_R_m2c': ab,
            'cam_t_m2c': ac,
            'obj_bb': [244, 150, 44, 58],
            'obj_id': 1
        }
    
#print(data)
with open(plst_pth, 'w') as f:
    yaml.dump(pdata, f, default_flow_style=None)
    f.close()
        

