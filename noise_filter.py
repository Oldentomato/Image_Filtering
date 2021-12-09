import numpy as np
import cv2
import shutil as sh
import os

file_list = os.listdir('./files')
success_count = 0
failed_count = 0
count = 0

print("필터링을 시작합니다 잠시만 기다려주세요")

for j in file_list:
    src = cv2.imread('./files/'+j)
    dst2 = cv2.bilateralFilter(src, d=-1, sigmaColor=50, sigmaSpace=50)
    mask = np.zeros((src.shape[0],src.shape[1],3),np.uint8)#새로운 검은 이미지를 만든다 (크기는 일반이미지크기에 맞춘다)
    gray = cv2.cvtColor(dst2, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 100, 200)
    lines = cv2.HoughLinesP(canny, 3.8, np.pi / 180, 100, minLineLength = 50, maxLineGap = 10)

    if lines is None: #HoughlinesP에서 선이 검출되지 않는다면 None으로 반환되기에 그것을 방지하기위함이다
        cv2.imwrite('./notfiltered/(notfilter)'+j,dst2)
        failed_count += 1
    else:
        for i in lines:
            cv2.line(mask, (i[0][0], i[0][1]), (i[0][2], i[0][3]), (0, 255, 0), 7) #마지막 매개변수가 선두께이다 선두께를 두껍게해야 잘 지워진다
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY) #라인그리기는 그레일스케일에서는 안되기때문에 라인을 그리고 그레이스케일로 바꿔야한다
        dst = cv2.inpaint(dst2,mask,3,cv2.INPAINT_TELEA)#마스크 이미지는 그레일스케일로 되어있어야한다
        cv2.imwrite('./filtered/(filter)'+j, dst)
        success_count += 1
    count+=1
    print ("이미지 필터링중 %.2f%%" % (count / len(file_list) * 100.0))
print("필터링완료 : "+ str(success_count)+"개 필터링이 되었고 "+ str(failed_count)+"개가 필터링이 되지 않았습니다")


