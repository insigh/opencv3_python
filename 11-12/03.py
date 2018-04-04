# -*- coding=GBK -*-
import cv2 as cv
# from matplotlib import pyplot as plt

import  matplotlib.pyplot as plt

#�����Աȶȣ�Ĭ����������ֻ���ǻҶ�ͼ��
def equalHist_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("ԭ   ��", gray)
    dst = cv.equalizeHist(gray)
    cv.imshow("Ĭ�ϴ���", dst)


#�Աȶ����ƣ��Զ�����ʾ������
def clahe_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(4, 4))
    dst = clahe.apply(gray)
    cv.imshow("�Զ��崦��", dst)

src = cv.imread("1.jpg")
equalHist_image(src)
clahe_image(src)
cv.waitKey(0)
cv.destroyAllWindows()