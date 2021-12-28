import cv2
import numpy as np
import canny_otsu as ot



def houghline(img,src,f_count, s_count):
    bilafilter = cv2.bilateralFilter(img, d=-1, sigmaColor=50,sigmaSpace=50)
    mask = np.zeros((img.shape[0], img.shape[1],3),np.uint8) #새로운 검은 이미지를 만든다(크기는 일반이미지크기에 맞춘다)
    gray = cv2.cvtColor(bilafilter,cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray,50,200)
    #3.8, 100, 50 , 10
    lines = cv2.HoughLinesP(canny, cv2.HOUGH_PROBABILISTIC, np.pi/180, 30, minLineLength=30, maxLineGap=5)

    if lines is None:#HoughlinesP에서 선이 검출되지 않는다면 None으로 반환되기에 그것을 방지하기위함이다
        cv2.imwrite('./notfiltered/(hough)'+src,ot.otsu_filter(bilafilter,False))
        f_count += 1
    else:
        for i in lines:
            cv2.line(gray, (i[0][0], i[0][1]), (i[0][2],i[0][3]), (0,255,0),7) #마지막 매개변수가 선두께이다 선두께를 두껍게해야 잘 지워진다
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY) #라인그리기는 그레일스케일에서는 안되기때문에 라인을 그리고 그레이스케일로 바꿔야한다
        dst = cv2.inpaint(bilafilter,mask,3,cv2.INPAINT_TELEA)#마스크 이미지는 그레일스케일로 되어있어야한다
        cv2.imwrite('./filtered/(hough)'+src,ot.otsu_filter(dst,False))
        s_count += 1

    return f_count,s_count
