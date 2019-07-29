import cv2
import numpy as np

#Create a Function to draw circle on the window at event click
def draw_circle(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:#left button click
        cv2.circle(img, (x,y), 100, (0,255,0), -1)
        
    elif event == cv2.EVENT_RBUTTONDOWN:#RIGHT BUTTON CLICK
        cv2.circle(img, (x,y), 100, (255,0,0), -1)
        
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_circle)
       
#creating/showing image with opencv
# img = np.zeros((512,512,3), np.int8)
img = np.zeros((512,512,3))
while True:
    cv2.imshow('my_drawing', img)
    
    #wait at least 20 milisecond till we press the esc key (27), then break out of the loop
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()