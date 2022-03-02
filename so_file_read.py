#!/usr/bin/env python3
import os
import pickle as pkl
import numpy as np
from plyfile import PlyData
import ctypes as ct


so_p = './rastertriangle_so.so'
dll = np.ctypeslib.load_library(so_p, '.')
print(dll)
