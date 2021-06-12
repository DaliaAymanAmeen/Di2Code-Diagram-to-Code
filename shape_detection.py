import numpy as np
import cv2
from collections import defaultdict

def shape_detection (image, image_type):
    """Function to separate the data type from the variable name and separate function name from return type

    Parameters
    ----------
    image : str
            The image path  

    Returns
    -------
    class_dictionary 
        dict #############
    
    relations 
        list #############
    """

    img = cv2.imread(image)
    img_h , img_w, _ = img.shape

    if (image_type == "computer"):
        if ((img_h >= 1000)  or (img_w >= 1000)):
            img = cv2.resize(img, None, fx=0.5, fy=0.5)
        if (((img_h < 1000) & (img_h>=550))  or ((img_w < 1000) & (img_w>=550))):
            img = cv2.resize(img, None, fx=1.1, fy=1.1, interpolation=cv2.INTER_CUBIC)
        if ((img_h < 550)  & (img_w < 550)):
            img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

    elif (image_type == "hand written"):
        if ((img_h >= 1000) or (img_w >= 800)):
            img = cv2.resize(img, None, fx=0.84, fy=0.95, interpolation=cv2.INTER_NEAREST)
            #img = cv2.resize(img, None, fx=0.8, fy=1.1, interpolation=cv2.INTER_CUBIC)
        if (((img_h < 1000) & (img_h >= 550)) or ((img_w < 1000) & (img_w >= 550))):
            img = cv2.resize(img, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC)
        if ((img_h < 550) & (img_w < 550)):
            img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

    #img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cv2.imshow("img", img)
    
    # list of (x,y) to store the coordinates of each detected rectangle
    coordinates = []
    relations = []

    # dictionary to store for example: class1: [(x_className,y_className), (x_attribute, y_attribute), (x_method, y_method)]
    class_dictionary = defaultdict(list)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)

        if len(approx) == 3:
            x = approx.ravel()[0]
            y = approx.ravel()[1] 
            if (image_type == "hand written"):
                if (cv2.contourArea(contour) > 120 and cv2.contourArea(contour) < 200):
                    cv2.drawContours(img, [approx], 0, (0, 0, 255), 2)
                    relations.append([x, y])
            elif (image_type == "computer"):
                if (cv2.contourArea(contour) > 30):
                    cv2.drawContours(img, [approx], 0, (0, 0, 255), 2)
                    relations.append([x, y])

        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            if ((w*h) > 1500):
                cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
                coordinates.append([x, y, w, h])
    
    if (image_type == "computer"):
        coordinates = sorted(coordinates, key=lambda x: x[0])
        coordinates.sort()

    elif(image_type == "hand written"):
        coordinates = sorted(coordinates, key=lambda x: x[1])

    i = -1
    x_prev = 0

    for rectangle in coordinates:
        x = rectangle[0]
        y = rectangle[1]
        w = rectangle[2]
        h = rectangle[3]

        if (x == 0): # the frame of the image (ignore it)
            continue
            
        if (x != x_prev and (x < (x_prev-10) or x > (x_prev+10))): # if it's not the same x (this is mean it's a new class)
            i += 1

        if (i == -1):
            i +=1

        class_dictionary[i].append([x, y, w, h])
        x_prev = x
        
    cv2.imshow("shapes", img)
    return class_dictionary, relations


    