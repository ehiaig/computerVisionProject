import cv2

img = cv2.imread('Photos/1.jpg')

while True:
    cv2.imshow('Converse', img)
# cv2.waitkey()

    #wait at least 1 milisecond till we press the esc key (27), then break out of the loop
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()