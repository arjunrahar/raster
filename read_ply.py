import numpy as np
import open3d as o3d
from plyfile import PlyData, PlyElement
import ctypes as ct
import cv2
import random

# Read .ply file
input_file = "obj_16.ply"
input1_file = "obj_01.ply"
pcd = o3d.io.read_point_cloud(input_file) # Read the point cloud
pcd1 = o3d.io.read_point_cloud(input1_file)
# Visualize the point cloud within open3d
#o3d.visualization.draw_geometries([pcd]) 

# Convert open3d format to numpy array
# Here, you have the point cloud in numpy format. 
pcd_in_numpy = np.asarray(pcd.points) 
pcd_in_numpy1 = np.asarray(pcd1.points) 
#print(type(pcd_in_numpy))
#print(pcd_in_numpy)
#print(pcd_in_numpy.shape)
#print(pcd_in_numpy1.shape)
#print(pcd_in_numpy)
#print(pcd_in_numpy1)
ply = PlyData.read(input_file)
print("ply", ply)
data = ply.elements[0].data
face_raw = ply.elements[1].data
print("face", face_raw)
#print(type(data))
x = data['x']
print("x", x)
print("data", data)
print("x shape", x.shape)
print("data shape", data.shape)
#print(x)
ply1 = PlyData.read(input1_file)
print("ply1", ply1)
data1 = ply1.elements[0].data
#d = np.dtype(data1)
#print(d.names)
x = data1['x']
print("x", x)
face_raw = ply1.elements[1].data
print("face", face_raw)
print("data1", data1)
print("x shape", x.shape)
print("data1 shape", data1.shape)

#print(type(data1))
#print(data.shape)
#print(data1.shape)

