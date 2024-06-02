import cv2 as cv
import mediapipe as mp
import time
from set_Motor import Motor1_x,Motor1_reverse_x,Motor2_y,Motor2_reverse_y

def Coordinate(boundBox):
    x1=boundBox[0]
    x2=x1+boundBox[2]
    y1=boundBox[1]
    y2=y1+boundBox[3]
    cx=(x1+x2)/2
    cy=(y1+y2)/2
    return cx,cy


def comparison_(sc_x_max,sc_x_min,sc_y_max,sc_y_min,bx_x,bx_y):
    if bx_x>sc_x_max or bx_x<sc_x_min:
        if bx_x>sc_x_max:
            Motor1_reverse_x(1)
        elif bx_x<sc_x_min:
            Motor1_x(1)
    if bx_y>sc_y_max or bx_y<sc_y_min:
        if bx_y>sc_y_max:
            Motor2_reverse_y(1)
        elif bx_y<sc_y_min:
            Motor2_y(1)
        
    # if bx_x==sc_x and bx_y==sc_y:
    #     return
    

def move_Motor(bx_x,bx_y):
    # sc_x=320
    sc_x_max=340
    sc_x_min=300
    # sc_y=240
    sc_y_max=260
    sc_y_min=220
    comparison_(sc_x_max,sc_x_min,sc_y_max,sc_y_min,bx_x,bx_y)
    return


def model():
    mp_facedetector = mp.solutions.face_detection
    mp_draw = mp.solutions.drawing_utils
    boundBox=[]
    cap = cv.VideoCapture(0)
    with mp_facedetector.FaceDetection(min_detection_confidence=0.7) as face_detection:
        
        while cap.isOpened():
            
            _, image = cap.read()
            start = time.time()
            
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            
            results = face_detection.process(image)
            
            image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
            
            if results.detections:
                for id, detection in enumerate(results.detections):
                    mp_draw.draw_detection(image, detection)
                    # print(id, detection)
                    
                    bBox = detection.location_data.relative_bounding_box           
                    h, w,_= image.shape
                    boundBox = int(bBox.xmin * w), int(bBox.ymin * h), int(bBox.width * w), int(bBox.height * h)
                    # print(boundBox[0],boundBox[1])
                    print(h,w,_)
                    box_x,box_y=Coordinate(boundBox)
                    print(box_x,box_y)
                    move_Motor(round(box_x),round(box_y))
            

            end = time.time()
            totalTime = end - start
            
            fps = 1 / totalTime
            print("FPS: ", fps)
            
            cv.putText(image, f'FPS: {int(fps)}', (20,70), cv.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)
            
            cv.imshow('Face Detection', image)
            key = cv.waitKey(1)
            if key==27:
                break
            
            
    cap.release()
    cv.destroyAllWindows()
        
def main():
    model()
main()
