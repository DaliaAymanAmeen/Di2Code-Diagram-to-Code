import classes 
import cv2 as cv
import shape_detection 
import draw
import class_creator 
import helper_functions as hf
import OCR
import os
import re
import webbrowser

classes_list = []
parent_class = "" 

def detection_button (image_type, path_ocr, path_shape):
    if (image_type == "computer"):
        image = path_shape

    elif (image_type == "handwritten"):
        image = path_shape
        image_ocr = path_ocr

    #shape dictionary
    shapes_dictionary, relations = shape_detection.shape_detection(image, image_type)
    if (image_type == "computer"):
        ocr_dictionary = OCR.computer_OCR(image)
    elif (image_type == "handwritten"):
        ocr_dictionary = OCR.handwritten_OCR(image_ocr)

    hf.create_instanse(shapes_dictionary, classes_list)

    for object in classes_list:
        object.is_parent(relations)
        data_type = object.data_type_matching(ocr_dictionary)
        if (image_type == "computer"):
            object.matching(ocr_dictionary, data_type)
        elif (image_type == "handwritten"): 
            object.matching_hand_written(ocr_dictionary, data_type)
        if (object.isParent):
            global parent_class
            parent_class = object.name

    draw.draw_diagram(classes_list, ocr_dictionary, "drawings_output/output.png")

    # create csv file to open using draw.io 
    draw.create_csv(classes_list, parent_class)

    #open draw.io then from Arrange> Insert> Advanced > CSV then copy the text in draw_csv file 
    url = 'https://app.diagrams.net/'
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)

    output_image = "drawings_output/output.png"
    csv_file = "drawings_output/draw_csv.csv"

    return output_image, csv_file


def code_generation (language):
    global parent_class
    if (language == "python"):
        class_creator.write_python_code(classes_list, parent_class)
        python_code = "generated code/python_code.py"
        os.startfile("generated code\python_code.py")
        return python_code
    elif (language == "cpp"):
        class_creator.write_cpp_code(classes_list, parent_class)
        cpp_h_code = "generated code/cpp_code.h"
        cpp_cpp_code = "generated code/cpp_code.cpp"
        os.startfile("generated code\cpp_code.h")
        os.startfile("generated code\cpp_code.cpp")
        return cpp_h_code, cpp_cpp_code

    
