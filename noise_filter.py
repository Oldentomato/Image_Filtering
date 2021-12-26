import cv2
import os
import houghline as hl

file_list = os.listdir('./files')
success_count = 0
failed_count = 0
count = 0

print("필터링을 시작합니다 잠시만 기다려주세요")

for j in file_list:
    src = cv2.imread('./files/'+j)
    if src is None: #이미지 이외의 파일이 읽혔을때 예외사항처리
        count += 1
        continue
    failed_count,success_count = hl.houghline(src,j,failed_count,success_count)
    count += 1
    print ("이미지 필터링중 %.2f%%" % (count / len(file_list) * 100.0))
print("필터링완료 : "+ str(success_count)+"개 필터링이 되었고 "+ str(failed_count)+"개가 필터링이 되지 않았습니다")


