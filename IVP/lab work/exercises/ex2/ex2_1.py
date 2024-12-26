import cv2 as cv
import mediapipe as mp
import matplotlib.pyplot as plt

mp_draw = mp.solutions.drawing_utils 

mp_pose = mp.solutions.pose 
pose = mp_pose.Pose(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) 

stat = str()
ac = t_ac = 0
ac_list = [] 
cap = cv.VideoCapture("ex2/test.mp4") 

cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920) 
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    frame = cap.read()[1]
    try:
        res = pose.process(cv.cvtColor(frame, cv.COLOR_BGR2RGB)) 
        landmarks = res.pose_landmarks 

        if landmarks is not None:
            x_min = frame.shape[1]
            y_min = frame.shape[0] 
            x_max = 0
            y_max = 0
            for landmark in landmarks.landmark: 
                x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]) 
                
                if x < x_min:
                    x_min = x
                if x > x_max:
                    x_max = x
                if y < y_min:
                    y_min = y
                if y > y_max:
                    y_max = y
            cv.rectangle(frame, (x_min, y_min - 10), (x_max, y_max + 20), (255, 0, 0), 2) 
            roi = frame[y_min - 10: y_max + 20, x_min: x_max]
            roi_gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
            thermal_roi = cv.applyColorMap(roi_gray, cv.COLORMAP_JET)
            frame[y_min - 10: y_max + 20, x_min: x_max] = thermal_roi
        cv.imshow('final', frame)
    except:
        break
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

plt.plot(ac_list)
plt.title('ACCURACY GRAPH')
plt.xlabel('FRAME')
plt.ylabel('ACCURACY')
plt.show()