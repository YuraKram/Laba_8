import cv2

cv2.namedWindow( "result" )
img = cv2.imread('variant-3.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
