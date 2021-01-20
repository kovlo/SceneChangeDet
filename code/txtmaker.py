import os
from pathlib import Path
import random
import cv2
import numpy as np
import matplotlib.pyplot as plt

def check_dir(dir):
    dir = str(dir)
    if not os.path.exists(dir):
        os.mkdir(dir)

image_sizeH = 128

rootdir = Path('/home/lorant/Projects/data/ChangeNet/combined/train')
outdirTr = Path('/home/lorant/Projects/data/ChangeNet/combined/train_sep')
t0dirTr = outdirTr/"t0"
t1dirTr = outdirTr/"t1"
gtdirTr = outdirTr/"gt_binary"
check_dir(t0dirTr)
check_dir(t1dirTr)
check_dir(gtdirTr)

outdirVal = Path('/home/lorant/Projects/data/ChangeNet/combined/val_sep')
t0dirVal = outdirVal/"t0"
t1dirVal = outdirVal/"t1"
gtdirVal = outdirVal/"gt_binary"
check_dir(t0dirVal)
check_dir(t1dirVal)
check_dir(gtdirVal)

traintxt = 'trainCD.txt'
valtxt  = 'valCD.txt'

with open(traintxt, 'w') as tr, open(valtxt, 'w') as vl:

    images = os.listdir(str(rootdir))
    images.sort()
    print(len(images))

    for gtimname in images:
        if random.random()<0.8:
            f=tr
            t0dir = t0dirTr
            t1dir = t1dirTr
            gtdir = gtdirTr
        else:
            f=vl
            t0dir = t0dirVal
            t1dir = t1dirVal
            gtdir = gtdirVal

        trio_img = cv2.imread(str(rootdir/gtimname),cv2.IMREAD_UNCHANGED)
        reference_img = trio_img[0:image_sizeH,:]/1000/42.42*255
        reference_img = np.tile(reference_img[:,:,np.newaxis],(1,1,3))
        test_img = trio_img[image_sizeH:2*image_sizeH,:]/1000/42.42*255
        test_img = np.tile(test_img[:,:,np.newaxis],(1,1,3))
        label_img = (trio_img[image_sizeH*2:,:]>0)*255
        label_img = np.tile(label_img[:,:,np.newaxis],(1,1,3))

        refpath   = str(t0dir/gtimname)
        testpath  = str(t1dir/gtimname)
        labelpath = str(gtdir/gtimname)
        cv2.imwrite(refpath,reference_img)
        cv2.imwrite(testpath,test_img)
        cv2.imwrite(labelpath,label_img)

        refpath   = str(Path(t0dir.parent.stem)/t0dir.stem/gtimname)
        testpath  = str(Path(t1dir.parent.stem)/t1dir.stem/gtimname)
        labelpath = str(Path(gtdir.parent.stem)/gtdir.stem/gtimname)

        savedirpath = Path(rootdir.parent.stem)/rootdir.stem
        a=str(savedirpath/gtimname)
        f.write(refpath+" "+testpath+" "+labelpath+"\n")
print('Done!')

## Test txt
testtxt = 'testCD.txt'
rootdir = Path('/home/lorant/Projects/data/ChangeNet/combined/test')
outdir = Path('/home/lorant/Projects/data/ChangeNet/combined/test_sep')
t0dir = outdir/"t0"
t1dir = outdir/"t1"
gtdir = outdir/"gt_binary"
check_dir(t0dir)
check_dir(t1dir)
check_dir(gtdir)

with open(testtxt, 'w') as tst:
   
    images = os.listdir(str(rootdir))
    images.sort()
    print(len(images))

    for gtimname in images:
        f=tst

        trio_img = cv2.imread(str(rootdir/gtimname),cv2.IMREAD_UNCHANGED)
        reference_img = trio_img[0:image_sizeH,:]/1000/42.42*255
        reference_img = np.tile(reference_img[:,:,np.newaxis],(1,1,3))
        test_img = trio_img[image_sizeH:2*image_sizeH,:]/1000/42.42*255
        test_img = np.tile(test_img[:,:,np.newaxis],(1,1,3))
        label_img = (trio_img[image_sizeH*2:,:]>0)*255
        label_img = np.tile(label_img[:,:,np.newaxis],(1,1,3))

        refpath   = str(t0dir/gtimname)
        testpath  = str(t1dir/gtimname)
        labelpath = str(gtdir/gtimname)
        cv2.imwrite(refpath,reference_img)
        cv2.imwrite(testpath,test_img)
        cv2.imwrite(labelpath,label_img)

        refpath   = str(Path(t0dir.parent.stem)/t0dir.stem/gtimname)
        testpath  = str(Path(t1dir.parent.stem)/t1dir.stem/gtimname)
        labelpath = str(Path(gtdir.parent.stem)/gtdir.stem/gtimname)

        savedirpath = Path(rootdir.parent.stem)/rootdir.stem
        a=str(savedirpath/gtimname)
        f.write(refpath+" "+testpath+" "+labelpath+"\n")
print('Done!')