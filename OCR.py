import cv2
import pytesseract
from collections import defaultdict
import numpy as np

#directory of tesseract executable file
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def computer_OCR(image):
    """OCR function to detect and extract words from a computerized image

    Parameters
    ----------
    image : str
            The image path  

    Returns
    -------
    class_dictionary 
        dict {str: list} the detected word and its associated coordinates
    
    """
    # read image, pre-processing
    img = cv2.imread(image)
    Img_h, Img_w, _ = img.shape
    #print(Img_h, Img_w)
    if ((Img_h >= 1000) or (Img_w >= 1000)):
        img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    if (((Img_h < 1000) & (Img_h >= 550)) or ((Img_w < 1000) & (Img_w >= 550))):
        img = cv2.resize(img, None, fx=1.1, fy=1.1, interpolation=cv2.INTER_CUBIC)
        kernel1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        img = cv2.filter2D(img, -1, kernel1)
    if ((Img_h < 550) & (Img_w < 550)):
        img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel2 = np.ones((1, 1), np.uint8)
    img = cv2.erode(img, kernel2, iterations=1)
    img = cv2.dilate(img, kernel2, iterations=1)
    config = ('-l eng --oem 1 --psm 3')

    # detecting words with boundary box
    boxes = pytesseract.image_to_data(img, config=config)
    # print(boxes)
    class_dictionary = defaultdict(list)
    coordinate_dictionary = defaultdict(list)
    i = 0
    for x, b in enumerate(boxes.splitlines()):
        # split output of fn
        if x != 0:
            b = b.split()
            # print(b)
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                coordinate_dictionary[i].append(x)
                coordinate_dictionary[i].append(y)
                class_dictionary[b[11]].append(coordinate_dictionary[i])
                i = i + 1
                cv2.rectangle(img, (x, y), (w + x, h + y), (0, 255, 0), 0)
                # cv2.putText(img, b[11], (x, y + h), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 20, 255), 0)

    # to show image
    #cv2.imshow('Result image', img)
    #cv2.waitKey(0)
    cv2.imwrite("drawings_output/ocr_computer.png",img)
    return class_dictionary


def handwritten_OCR(image):
    """OCR function to detect and extract words from a handwritten image

    Parameters
    ----------
    image : str
            The image path  

    Returns
    -------
    class_dictionary 
        dict {str: list} the detected word and its associated coordinates
    
    """
    # read image, pre-processing
    img = cv2.imread(image)
    Img_h, Img_w, _ = img.shape
    #print(Img_h, Img_w)
    if ((Img_h >= 1000) or (Img_w >= 800)):
        img = cv2.resize(img, None, fx=0.84, fy=0.95, interpolation=cv2.INTER_NEAREST)
        #img = cv2.resize(img, None, fx=0.8, fy=1.1, interpolation=cv2.INTER_CUBIC)
    if (((Img_h < 1000) & (Img_h >= 550)) or ((Img_w < 1000) & (Img_w >= 550))):
        img = cv2.resize(img, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC)
    if ((Img_h < 550) & (Img_w < 550)):
        img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    #kernel1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    #img = cv2.filter2D(img, -1, kernel1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel2 = np.ones((1, 1), np.uint8)
    img = cv2.erode(img, kernel2, iterations=1)
    img = cv2.dilate(img, kernel2, iterations=1)
    config = ('-l eng --oem 3 --psm 6')

    # detecting words with boundary box
    boxes = pytesseract.image_to_data(img, config=config)
    # print(boxes)
    class_dictionary = defaultdict(list)
    coordinate_dictionary = defaultdict(list)
    i = 0
    for x, b in enumerate(boxes.splitlines()):
        # split output of fn
        if x != 0:
            b = b.split()
            # print(b)
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                coordinate_dictionary[i].append(x)
                coordinate_dictionary[i].append(y)
                class_dictionary[b[11]].append(coordinate_dictionary[i])
                i = i + 1
                cv2.rectangle(img, (x, y), (w + x, h + y), (0, 255, 0), 0)
                # cv2.putText(img, b[11], (x, y + h), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 20, 255), 0)


    # to show image
    #cv2.imshow('Result image', img)
    cv2.imwrite("drawings_output/ocr_handwritten.png",img)
    cv2.waitKey(0)
    print(class_dictionary)
    return class_dictionary









