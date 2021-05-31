import shape_detection 
import cv2

print (shape_detection.shape_detection("test_images/test_image.png"))

cv2.waitKey(0)
cv2.destroyAllWindows()