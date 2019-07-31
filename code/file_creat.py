import glob
import os

base_path='/home/z/PycharmProjects/dataset_/TSUNAMI/'
# path1=base_path+'/t0/*.jpg'
# all_path1=glob.glob(path1)
# path2=base_path+'/t1/*.jpg'
# all_path2=glob.glob(path2)
# path3=base_path+'/ground_truth/*.bmp'
# all_ground=glob.glob()
def read_file(base_path,step_path,file_tpye):
    path=base_path+'/'+step_path+'/*.'+str(file_tpye)
    all_path=glob.glob(path)
    all_path.sort()
    return all_path

t0=read_file(base_path,'t0','jpg')
t1=read_file(base_path,'t1','jpg')
gt=read_file(base_path,'ground_truth','bmp')

with open('1.txt' ,'a') as f:
    for i in range(len(t0)):
        value=t0[i],' ',t1[i],' ',gt[i],'_n'
        value=str(value)
        value=value.replace('[','').replace(']','').replace('(','').replace(')','').replace(',','').replace("'",'').replace('_n','\n')
        f.write(value)
