import cv2
import canny_otsu as ot
import numpy as np

def contour(img,src,s_count):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    mask = np.zeros((img.shape[0], img.shape[1],3),np.uint8)

    #쓰레시홀드로 바이너리 이미지를 만들어 검은 배경에 흰색전경으로 반전
    ret,imgthres = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

    #contours는 검출된 컨투어 좌표리스트, hierarchy는 해당 컨투어의 계층정보 배열
    contours,hierarchy = cv2.findContours(imgthres,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #매개변수에 -1부분은 계층별 구분인데 -1은 모든 계층을 나타낸다
    cv2.drawContours(mask,contours,-1,(255,255,255),4)

    mask = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
    result = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
    result = cv2.bilateralFilter(result, d=-1, sigmaColor=50,sigmaSpace=50)
    cv2.imwrite('./filtered/(contour)'+src, ot.otsu_filter(result,False))
    s_count += 1
    return s_count