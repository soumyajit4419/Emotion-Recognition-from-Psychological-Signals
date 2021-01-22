import pandas as pd
import numpy as np
import os
import pickle
from shutil import copy


# Getting Arousal Lables of user
arousal_label = []
for i in range(1, 11):
    x = pickle.load(open("../Dataset/UserLabels/User" +
                         str(i) + "/user_labels.pkl", "rb"))
    ar = []
    for j in range(len(x)):
        ar.append(x[j][0])
    arousal_label.append(ar)


# Getting Valence Lables of user
valence_label = []
for i in range(1, 11):
    x = pickle.load(open("../Dataset/UserLabels/User" +
                         str(i) + "/user_labels.pkl", "rb"))
    ar = []
    for j in range(len(x)):
        ar.append(x[j][1])
    valence_label.append(ar)


images = os.listdir("./CNNImages/")


# Creating Folders
try:
    os.mkdir("./Arousal")
    print("Folder Created")
except:
    print("Folder Exits")


try:
    os.mkdir("./Arousal/High")
    print("Folder Created")
except:
    print("Folder Exits")


try:
    os.mkdir("./Arousal/Low")
    print("Folder Created")
except:
    print("Folder Exits")


try:
    os.mkdir("./Valence")
    print("Folder Created")
except:
    print("Folder Exits")


try:
    os.mkdir("./Valence/High")
    print("Folder Created")
except:
    print("Folder Exits")


try:
    os.mkdir("./Valence/Low")
    print("Folder Created")
except:
    print("Folder Exits")


# Putting the images in respective folder according to arousal
for i in range(len(images)):

    img = images[i]
    usr = img.split('_')
    user_no = usr[0].split('r')
    user_no = user_no[1]
    user_no = int(user_no)

    vid_no = usr[1].split('.')
    vid_no = vid_no[0].split('d')
    vid_no = vid_no[1].split('&')
    vid_no = vid_no[0]
    vid_no = int(vid_no)

    val = arousal_label[user_no-1][vid_no-1]
    if(val >= 4.5):
        copy("./CNNImages/"+img, "./Arousal/High/")
    else:
        copy("./CNNImages/"+img, "./Arousal/Low/")


# Putting the images in respective folder according to valence
for i in range(len(images)):

    img = images[i]
    usr = img.split('_')
    user_no = usr[0].split('r')
    user_no = user_no[1]
    user_no = int(user_no)

    vid_no = usr[1].split('.')
    vid_no = vid_no[0].split('d')
    vid_no = vid_no[1].split('&')
    vid_no = vid_no[0]
    vid_no = int(vid_no)

    val = valence_label[user_no-1][vid_no-1]
    if(val >= 4.5):
        copy("./CNNImages/"+img, "./Valence/High/")
    else:
        copy("./CNNImages/"+img, "./Valence/Low/")
