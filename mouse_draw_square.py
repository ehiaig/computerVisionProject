import cv2
import numpy as np

drawing = False
ix, iy = -1, -1

def draw_rectangle(event, x,y,flags,params):
    
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
        

#Draw Black Image
img  = np.zeros((512,512,3))

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_rectangle)

while True:
    cv2.imshow('my_drawing', img)
    
    #wait at least 1 milisecond till we press the esc key (27), then break out of the loop
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()