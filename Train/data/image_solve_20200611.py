# import cv2
# import os
# path = './image_all'
# train_image_path = './new'
# with open('./correct_train.txt','r') as f:
#     for i in f:
#         name = i.strip(' ').split(' ')[0]
#         print(name)
#         image_path = os.path.join(path,name)
#         img = cv2.imread(image_path)
#         new_image_path = os.path.join(train_image_path,name)
#         cv2.imwrite(new_image_path,img)
#         # cv2.imshow('img',img)
#         # cv2.waitKey(0)

import torch

a = torch.Tensor([[1,2,4,5],[1,2,4,5]])[0].transpose(1, 0).contiguous().view(-1)
print(a.max(0))