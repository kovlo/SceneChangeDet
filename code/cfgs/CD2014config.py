import os

BASE_PATH = '/home/lorant/Projects/data/SceneChangeDet'
PRETRAIN_MODEL_PATH = os.path.join(BASE_PATH,'pretrain')
# DATA_PATH = '/media/admin228/0007A0C30005763A/datasets/dataset_/CD2014'
DATA_PATH = '/home/lorant/Projects/data/ChangeNet/combined'
TRAIN_DATA_PATH = os.path.join(DATA_PATH,'')
TRAIN_LABEL_PATH = os.path.join(DATA_PATH,'')
TRAIN_TXT_PATH = os.path.join(DATA_PATH,'trainCD.txt')
VAL_DATA_PATH = os.path.join(DATA_PATH,'')
VAL_LABEL_PATH = os.path.join(DATA_PATH,'')
VAL_TXT_PATH = os.path.join(DATA_PATH,'valCD.txt')
TEST_DATA_PATH = os.path.join(DATA_PATH,'')
TEST_LABEL_PATH = os.path.join(DATA_PATH,'')
TEST_TXT_PATH = os.path.join(DATA_PATH,'testCD.txt')
SAVE_PATH ='/home/lorant/Projects/data/SceneChangeDet/trainoutputCD'
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
# TRANSFROM_SCALES = (w,h)
TRANSFROM_SCALES= (1024,128)
#TRANSFROM_SCALES= (512,512)
T0_MEAN_VALUE = (107.800,117.692,119.979)
T1_MEAN_VALUE = (110.655,117.107,119.135)
    

