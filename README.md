# Image_Filtering
> 머신러닝을 위한 이미지 필터링

[이미지다운로드](https://www.kaggle.com/surajghuwalewala/ham1000-segmentation-and-classification)   
[이미지복원참고](http://www.gisdeveloper.co.kr/?p=7193)   
[직선검출참고](https://076923.github.io/posts/Python-opencv-28/)   
[등고선검출참고1](https://stackoverflow.com/questions/26561893/laser-curved-line-detection-using-opencv-and-python)   
[등고선검출참고2](https://bkshin.tistory.com/entry/OpenCV-22-%EC%BB%A8%ED%88%AC%EC%96%B4Contour)

- bilateralFilter를 이용하여 이미지 노이즈를 삭제해주고 Canny와 HoughLinesP를 이용하여 직선을 색출하고 지워주는 작업을 수행합니다. 하지만 곡선이 너무 많기에 제대로 검출되지않아 채택하지 않았습니다.



- 색깔검출(inRange)를 활용하여 제거하려 했지만 털의 색상이 너무 다양하여 채택하지 않았습니다.   


- (최종) 등고선(contour)을 활용하여 높낮이를 이용한 외곽선 검출을 시도했습니다. 원래 의도라면 털은 무조건 피부위에 있어야하기에 최하위 계층인 점조직을 제외하고 다른 모든 계층을 지우려는 목적이었으나 구현이 까다로워 모양의 변화가 조금 있으나 전체 검출로 하였고, 내부 면적이나 꼭짓점검출 등 여러 기능들이 있어 이 방법을 채택하였습니다.   

**위 방법을 이용하여 털제거후 canny_otsu를 이용하여 점조직의 윤곽선을 검출**   


>noise_filter에서 각 함수별 사용으로 된부분들은 반드시 하나씩만 주석해제하여 실행할것
