import cv2
import numpy as np
img = cv2.imread('SOfaOutput_img.png')
LegInImg = cv2.imread('sofawithleg.jpg')
LegInImgRight = cv2.flip(LegInImg, 1)
list = [LegInImgRight,LegInImg]
Repleg = cv2.imread('leg.jpg')

for i in list:
  res = cv2.matchTemplate(img, i, cv2.TM_CCOEFF_NORMED)
  loc = np.where (res >=  0.98)
  for i in range(len(loc[0])):
    posToDelete = (loc[0][i], loc[1][i])
    posToAdd = (loc[0][i] -1  , loc[1][i]) # -1 pixels up  +1 pixles down (if need)
    posToAdd = (max(0, min(posToAdd[0],img.shape[0]-1 -Repleg.shape[0] )) , max(0, min(posToAdd[1],img.shape[1]-1-Repleg.shape[1])))
    #img[posToDelete[0]:posToDelete[0] + LegInImg.shape[0],posToDelete[1]:posToDelete[1] + LegInImg.shape[1]] = (255,255,255)
    img[posToAdd[0]:posToAdd[0] + Repleg.shape[0], posToAdd[1]:posToAdd[1] + Repleg.shape[1]] = Repleg
  if i != 1:
    Repleg = cv2.flip(Repleg, 1)
    pass
cv2.imshow("Frame", img)
#cv2.imwrite("NIce_output.png",img)
cv2.waitKey(0)
