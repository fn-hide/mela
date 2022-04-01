import os
import shutil

import pandas as pd
import cv2 as cv

from glob import glob
from time import sleep


filepaths = glob('c:/users/labkom2-12/downloads/dull/content/jpeg128x128/dull/*downsampled.jpg')
ground_truth = pd.read_csv('c:/users/labkom2-12/downloads/dull/train.csv')
label = ground_truth[['image_name', 'diagnosis']]
print(label.head())
os.listdir('c:/users/labkom2-12/downloads/dull/')
os.mkdir('c:/users/labkom2-12/downloads/dull/Downsampled')
for filepath in filepaths:
    print(filepath)
    
# move downsampled to specified folder
downsampleds = glob('c:/users/labkom2-12/downloads/dull/content/jpeg128x128/dull/*downsampled.jpg')
# downsampleds
for downsampled in downsampleds:
    # print(downsampled)
    filename = downsampled.split('\\')[-1]
    shutil.move(downsampled, f'c:/users/labkom2-12/downloads/dull/Downsampled/{filename}')

len(os.listdir('c:/users/labkom2-12/downloads/dull/content/jpeg128x128/dull'))
len(os.listdir('c:/users/labkom2-12/downloads/dull/downsampled'))


os.mkdir('c:/users/labkom2-12/downloads/dull/Batch 2')
os.mkdir('c:/users/labkom2-12/downloads/dull/Batch 3')

new_samples = glob('c:/users/labkom2-12/downloads/dull/content/jpeg128x128/dull/*.jpg')
maxval = len(new_samples)//2
n = 0

for sample in new_samples:
    filename = sample.split('\\')[-1]
    # print(filename)
    shutil.move(sample, f'c:/users/labkom2-12/downloads/dull/Batch 2/{filename}')
    if n > maxval:
        break
    n += 1

len(os.listdir('c:/users/labkom2-12/downloads/dull/content/jpeg128x128/dull/'))
# memindahkan sisanya ke Batch 3

last_samples = glob('c:/users/labkom2-12/downloads/dull/content/jpeg128x128/dull/*.jpg')
for lsample in last_samples:
    filename = lsample.split('\\')[-1]
    shutil.move(lsample, f'c:/users/labkom2-12/downloads/dull/Batch 3/{filename}')

os.listdir('c:/users/labkom2-12/downloads/dull/')
os.mkdir('c:/users/labkom2-12/downloads/dull/Temp')
# batch 1 adalah citra campuran

filepaths1 = glob('c:/users/labkom2-12/downloads/dull/Batch 1/*.jpg')
filepaths2 = glob('c:/users/labkom2-12/downloads/dull/Batch 2/*.jpg')
len(filepaths1)
len(filepaths2)

for filepath1 in filepaths1:
    filename = filepath1.split('\\')[-1]
    shutil.move(filepath1, f'c:/users/labkom2-12/downloads/dull/Temp/{filename}')

for filepath2 in filepaths2:
    filename = filepath2.split('\\')[-1]
    shutil.move(filepath2, f'c:/users/labkom2-12/downloads/dull/Temp/{filename}')

kelas = list(label.diagnosis.unique())

for kls in kelas:
    os.mkdir(f'c:/users/labkom2-12/downloads/dull/Temp/{kls}')

label.diagnosis.unique()
label.info()
label.diagnosis.value_counts()

os.listdir('c:/users/labkom2-12/downloads/dull/Temp')
os.mkdir('c:/users/labkom2-12/downloads/dull/Temp/basket')

filepaths_basket = glob('c:/users/labkom2-12/downloads/dull/temp/*.jpg')
for filepath_basket in filepaths_basket:
    filename = filepath_basket.split('\\')[-1]
    shutil.move(filepath_basket, f'c:/users/labkom2-12/downloads/dull/temp/basket/{filename}')
    

filepaths_all = glob('c:/users/labkom2-12/downloads/dull/temp/basket/*.jpg')
len(filepaths_all)

for filepath_all in filepaths_all:
    filename = filepath_all.split('\\')[-1]
    print(filename)
    
for i in range(len(label)):
    filepath = f'c:/users/labkom2-12/downloads/dull/temp/basket/{label.image_name[i]}.jpg'
    if os.path.exists(filepath):
        # print(label.image_name[i], label.diagnosis[i])
        shutil.move(filepath, f'c:/users/labkom2-12/downloads/dull/temp/{label.diagnosis[i]}/{label.image_name[i]}.jpg')

for i in os.listdir('c:/users/labkom2-12/downloads/dull/temp/'):
    print(i, len(os.listdir('c:/users/labkom2-12/downloads/dull/temp/' + i)))



