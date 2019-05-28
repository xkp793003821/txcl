#coding:utf-8
import cv2
import numpy as np

path='/home/cooper/PycharmProjects/txcl/2.png'


image=cv2.imread(path)

tihuan=np.zeros_like(image)
for i in range(3):
    tihuan[:,:,i]=image[:,:,2-i]
cv2.imwrite('4tihuan.jpg',tihuan)
cv2.imwrite('4image.jpg',image)


cv2.imwrite('4blue_chanell.jpg',cv2.merge([image[:,:,0],np.zeros_like(image[:,:,0],np.uint8),np.zeros_like(image[:,:,0],np.uint8)]))
cv2.imwrite('4green_chanell.jpg',cv2.merge([np.zeros_like(image[:,:,0],np.uint8),image[:,:,1],np.zeros_like(image[:,:,0],np.uint8)]))
cv2.imwrite('4red_chanell.jpg',cv2.merge([np.zeros_like(image[:,:,0],np.uint8),np.zeros_like(image[:,:,0],np.uint8),image[:,:,2]]))



zengqiang=np.zeros_like(image,np.uint8)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i][j][1]>image[i][j][0] and image[i][j][1]>image[i][j][2] and image[i][j][1]>100 and image[i][j][2]<200 and image[i][j][0]<200:
            image[i][j][1]=min(255,image[i][j][1]*2)
            image[i][j][0]=image[i][j][0]//2
            image[i][j][2]=image[i][j][2]//2


cv2.imwrite('4green_zengqiang.jpg',image)
cv2.waitKey(0)