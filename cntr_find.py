# 컨투어 찾기와 그리기 (cntr_find.py)

import cv2
import numpy as np

img = cv2.imread('C:/Users/seunggu/Desktop/digital_imageprocessing/shapes.png')
img2 = img.copy()

# 그레이 스케일로 변환 ---①
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 가장 바깥쪽 컨투어에 대해 모든 좌표 반환 ---③
contour, hierarchy = cv2.findContours(imgray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 모든 좌표를 갖는 컨투어 그리기, 초록색  ---⑥
cv2.drawContours(img, contour, -1, (0,255,0), 4)
lst = ['Hexagon','Triangle','Pentagon','Circle','Rectangle']

# 컨투어 모든 좌표를 작은 파랑색 점(원)으로 표시 ---⑧
for idex , i in enumerate(contour):
    cv2.putText(img,lst[idex],tuple(i[0][0],), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

# 결과 출력 ---⑩
# cv2.putText(img, "Text" , (10,10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
cv2.imshow('CHAIN_APPROX_NONE', img)
cv2.waitKey(0)
cv2.destroyAllWindows()