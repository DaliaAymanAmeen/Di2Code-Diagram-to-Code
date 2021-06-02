import numpy as np
import cv2
from collections import defaultdict

def shape_detection (image):

    img = cv2.imread(image)
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cv2.imshow("img", img)
    counter = 0
    coordinates = []
    #diction gowah classA :: list[classname(),att(),method()]
    #nfs el x teb2a nfs el class, w b tarteb el y hn3rf 
    class_dictionary = defaultdict(list)
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
        #if len(approx) == 3:
            #cv2.drawContours(img, [approx], 0, (0, 0, 0), 2)
        if len(approx) == 4:
            x1, y1, w, h = cv2.boundingRect(approx)
            if ((w*h) > 1500):
                cv2.drawContours(img, [approx], 0, (0, 0, 0), 2)
                counter += 1
                x = approx.ravel()[0]
                y = approx.ravel()[1] - 5
                coordinates.append([x, y])
    
    coordinates = sorted(coordinates, key=lambda x: x[0])
    coordinates.sort()

    print(coordinates)
    i = 0
    x_prev = 0
    for rectangle in coordinates:
        x = rectangle[0]
        y = rectangle[1]
        if (x == 0):
            continue
        if (x != x_prev):
            i += 1
        class_dictionary[i].append([x,y])
        x_prev = x
    cv2.imshow("shapes", img)
    return class_dictionary


