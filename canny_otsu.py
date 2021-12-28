import cv2


def otsu_filter(img,isgray=True):
	if isgray is False:
		img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#그레이스케일로 바꾸는 이유는 threshold에서 3채널 이미지를 인자로 넘기면(otsu한정)
	#THRESH_OTSU mode:>'src_type==CV_8UC1||src_type==CV_16UC1'에러가 발생하기 때문이다

	blur = cv2.GaussianBlur(img,(5,5),0)
	_, th4 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	#50,150
	th5 = cv2.Canny(th4,100,200)


	return th5

