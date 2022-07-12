# import necessary packages
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2

index = 0
webcam = cv2.VideoCapture(0) # open webcam (웹캠 열기)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

while webcam.isOpened(): # loop through frames

    status, frame = webcam.read() # read frame from webcam
    if not status: break
    bbox, label, conf = cv.detect_common_objects(frame) # apply object detection (물체 검출)

    # draw bounding box over detected objects (검출된 물체 가장자리에 바운딩 박스 그리기)
    out = draw_bbox(frame, bbox, label, conf, write_conf=True)

    # display output
    cv2.imshow("Real-time object detection", out)
    set_label = set(label) # 중복 제거
    label = list(set_label)
    for i in range(0,len(label)):
        if label[i] == 'person': # person이 배열에 있으면 인덱스 추가
            index += 1
            print(index)
    if index == 10: # 일정 시간 지속적으로 포착되면 알림 출력
        print ("수상한 사람이 포착되었습니다.")
        index = 0
    if 'person' not in label: # 카메라에 사람이 없으면 인덱스 초기화
        index = 0
    if cv2.waitKey(1) & 0xFF == ord('q'): # q를 누르면 카메라 종료
        break
    print(label)
webcam.release()
cv2.destroyAllWindows()
