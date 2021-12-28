import cv2
import canny_otsu as ot

def colordetect(img,src,f_count,s_count):
    
    # hsv = cv2.cvtColor(bilafilter,cv2.COLOR_BGR2HSV)
    colordetect = cv2.inRange(img, (0,0,0),(100,100,100))


    if colordetect is None:
        bilafilter = cv2.bilateralFilter(img, d=-1, sigmaColor=50,sigmaSpace=50)
        cv2.imwrite('./notfiltered/(color)'+src,ot.otsu_filter(bilafilter,False))
        f_count += 1
    else:
        result = cv2.inpaint(img,colordetect,3,cv2.INPAINT_TELEA)
        cv2.imwrite('./filtered/(color)'+src,ot.otsu_filter(result,False))
        s_count += 1
    return f_count,s_count