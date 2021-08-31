


from skimage.io import imread, imshow
import matplotlib.pyplot as plt

from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data
from skimage.color import label2rgb

import numpy as np
import tkinter
from tkinter.filedialog import askopenfilename
from skimage.transform import resize
import cv2
INP = []
Trainfea3 = []
#import tkinter as tk
from tkinter.filedialog import askopenfilename
#tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

# GETTING INPUT DATA
for ijk in range(0,31):
    temp = ijk+1
    FL = 'Dataset\IMM ('
    FL1 = ').jpg'
    fnum = str(temp)
    I = imread(FL+fnum+FL1, as_gray=False)


    img_resized = resize(I, (300, 300))


    img_resized_r = img_resized[:,:,0]
    img_resized_g = img_resized[:,:,1]
    img_resized_b = img_resized[:,:,2]



# FEATURE EXTRACTION

    MN_r = np.mean(img_resized[:,:,0])
    ST_r = np.std(img_resized[:,:,0])
    Var_r = np.var(img_resized[:,:,0])

    MN_g = np.mean(img_resized[:,:,1])
    ST_g = np.std(img_resized[:,:,1])
    Var_g = np.var(img_resized[:,:,1])

    MN_b = np.mean(img_resized[:,:,2])
    ST_b = np.std(img_resized[:,:,2])
    Var_b = np.var(img_resized[:,:,2])


    Testfea1 = [MN_r,ST_r,Var_r]
    Testfea2 = [MN_g,ST_g,Var_g]
    Testfea3 = [MN_b,ST_b,Var_b]


    Hash_val = [hash(tuple(Testfea1)),hash(tuple(Testfea2)),hash(tuple(Testfea3))]




    Trainfea3.append(Hash_val)

        
import pickle
with open('Trainfea_new.pickle', 'wb') as f:
    pickle.dump(Trainfea3, f)