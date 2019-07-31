
path1='/home/z/PycharmProjects/dataset_/cd2014/backup/train.txt'
path2='/home/z/PycharmProjects/dataset_/cd2014/backup/val.txt'
path3='/home/z/PycharmProjects/dataset_/cd2014/val.txt'
path4='/home/z/PycharmProjects/dataset_/cd2014/train.txt'


b=[x for x in open(path1).readlines() if x.find('PTZ')>-1]
with open(path4,'w') as f:
    f.writelines(b)
    print('saved train')
c=[x for x in open(path2).readlines() if x.find('PTZ')>-1]
with open(path3,'w') as f:
    f.writelines(c)
    print('saved val')
