from train import *


TEST_TXT_PATH= '/home/lorant/Projects/data/SceneChangeDet/cd2014/test.txt'

test_data = dates.Dataset(cfg.VAL_DATA_PATH,cfg.VAL_LABEL_PATH,
                            TEST_TXT_PATH,'val',transform=False)
test_dataloader = Data.DataLoader(test_data, batch_size= cfg.BATCH_SIZE,
                                shuffle= False, num_workers= 4, pin_memory= True)

base_seg_model = 'deeplab'

import model.siameseNet.deeplab_v2 as models
model = models.SiameseNet(norm_flag='l2')
print(cfg.TRAINED_BEST_PERFORMANCE_CKPT)
checkpoint = torch.load(cfg.TRAINED_BEST_PERFORMANCE_CKPT)
model.load_state_dict(checkpoint['state_dict'])
print('resume success')
model = model.cuda()
model.eval()

print("alma")
for batch_idx, batch in enumerate(test_dataloader):
    inputs1,input2, targets, filename, height, width = batch
    print(filename)
    
    height, width, filename = height.numpy()[0], width.numpy()[0], filename[0]
    inputs1,input2,targets = inputs1.cuda(),input2.cuda(), targets.cuda()
    inputs1,inputs2,targets = Variable(inputs1, volatile=True),Variable(input2,volatile=True) ,Variable(targets)
    
    out_conv5,out_fc,out_embedding = model(inputs1,inputs2)
    out_conv5_t0, out_conv5_t1 = out_conv5
    out_fc_t0,out_fc_t1 = out_fc
    out_embedding_t0,out_embedding_t1 = out_embedding
    conv5_distance_map = single_layer_similar_heatmap_visual(out_conv5_t0,out_conv5_t1,save_change_map_dir,epoch,filename,'conv5','l2')
    fc_distance_map = single_layer_similar_heatmap_visual(out_fc_t0,out_fc_t1,save_change_map_dir,epoch,filename,'fc','l2')
    embedding_distance_map = single_layer_similar_heatmap_visual(out_embedding_t0,out_embedding_t1,save_change_map_dir,epoch,filename,'embedding','l2')
    
    '''
    cont_conv5 = mc.RMS_Contrast(conv5_distance_map)
    cont_fc = mc.RMS_Contrast(fc_distance_map)
    cont_embedding = mc.RMS_Contrast(embedding_distance_map)
    cont_conv5_total += cont_conv5
    cont_fc_total += cont_fc
    cont_embedding_total += cont_embedding
    num += 1
    '''
    prob_change = embedding_distance_map[0][0]
    gt = targets.data.cpu().numpy()
    fc_distance_map_CPU = fc_distance_map.data.cpu().numpy()
      
    testoutput_dir = os.path.join(cfg.SAVE_PRED_PATH,'testoutput')
    check_dir(testoutput_dir)
    

    cv2.imwrite(os.path.join(testoutput_dir,filename,'.png'),fc_distance_map)
    cv2.imwrite(os.path.join(testoutput_dir,filename,'_cpu.png'),fc_distance_map_CPU)
    print('ciklus vege')