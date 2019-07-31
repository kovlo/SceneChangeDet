import os

BASE_PATH = '/home/z/PycharmProjects/dataset_/base_path/'
PRETRAIN_MODEL_PATH = os.path.join(BASE_PATH,'pretrain')
# DATA_PATH = '/media/admin228/0007A0C30005763A/datasets/dataset_/CD2014'
DATA_PATH = '/home/z/PycharmProjects/dataset_/cd2014/'
TRAIN_DATA_PATH = os.path.join(DATA_PATH,'dataset')
TRAIN_LABEL_PATH = os.path.join(DATA_PATH,'dataset')
TRAIN_TXT_PATH = os.path.join(DATA_PATH,'train.txt')
VAL_DATA_PATH = os.path.join(DATA_PATH,'dataset')
VAL_LABEL_PATH = os.path.join(DATA_PATH,'dataset')
VAL_TXT_PATH = os.path.join(DATA_PATH,'val.txt')
TEST_DATA_PATH = os.path.join(DATA_PATH,'dataset')
TEST_TXT_PATH = os.path.join(DATA_PATH,'val.txt')
SAVE_PATH = '/home/z/PycharmProjects/dataset_/save_path/'
if not os.path.exists(SAVE_PATH):
    os.mkdir(SAVE_PATH)
SAVE_CKPT_PATH = os.path.join(SAVE_PATH,'ckpt')
if not os.path.exists(SAVE_CKPT_PATH):
    os.makedirs(SAVE_CKPT_PATH)
SAVE_PRED_PATH = os.path.join(SAVE_PATH,'prediction')
if not os.path.exists(SAVE_PRED_PATH):
    os.makedirs(SAVE_PRED_PATH)
TRAINED_BEST_PERFORMANCE_CKPT = os.path.join(SAVE_CKPT_PATH,'model_best.pth')
print os.listdir(SAVE_CKPT_PATH)
INIT_LEARNING_RATE = 1e-7
DECAY = 5e-5
MOMENTUM = 0.9
MAX_ITER = 40000
BATCH_SIZE = 1
THRESH = 0.5
THRESHS = [0.1,0.3,0.5]
LOSS_PARAM_CONV = 3
LOSS_PARAM_FC = 3
# TRANSFROM_SCALES= (512,512)
TRANSFROM_SCALES= (570,340)
T0_MEAN_VALUE = (107.800,117.692,119.979)
T1_MEAN_VALUE = (110.655,117.107,119.135)
    

