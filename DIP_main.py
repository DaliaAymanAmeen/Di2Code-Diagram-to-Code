import cv2
import classes 
import shape_detection 
import draw
import class_creator 
import OCR
import re
import webbrowser

#image_type = "hand written"
image_type = "computer"

if (image_type == "computer"):
    image = "test_images/new.png"
elif (image_type == "hand written"):
    image = "test_images/hand_written_final.jpeg" 
    image_ocr = "test_images/hand_written_final_ocr.jpeg" 

#shape dictionary
#shapes_dictionary, relations = shape_detection.shape_detection(image)
shapes_dictionary, relations = shape_detection.shape_detection(image, image_type)
print (shapes_dictionary)
print (relations)

#ocr dictionary 
#ocr_dictionary = {'Person': [[189, 14]], '‘age:': [[152, 46]], 'int': [[201, 42], [250, 74]], 'get_age()': [[152, 73]], ':': [[236, 79], [37, 327], [333, 327], [99, 355], [361, 355]], 'Student': [[45, 294]], 'Professor': [[315, 294]], 'id': [[14, 321]], 'str': [[50, 323], [346, 324]], 'title': [[292, 321]], 'get_gpa()': [[13, 349]], 'float': [[113, 350]], 'teach()': [[291, 349]], 'None': [[372, 350]]}
if (image_type == "computer"):
    ocr_dictionary = OCR.computer_OCR(image)
elif (image_type == "hand written"):
    ocr_dictionary = OCR.handwritten_OCR(image_ocr)
print (ocr_dictionary)

# to create instance for each class 
classes_list = []
for i in range (len(shapes_dictionary)):
    new_class = classes.Classes()
    # class name info
    new_class.name_coordinates =  shapes_dictionary[i][0]
    new_class.name_lower_limit.append(shapes_dictionary[i][0][0] - 10)
    new_class.name_lower_limit.append(shapes_dictionary[i][0][1] - 5)
    new_class.name_upper_limit.append(shapes_dictionary[i][0][0] + shapes_dictionary[i][0][2])
    new_class.name_upper_limit.append(shapes_dictionary[i][0][1]+ shapes_dictionary[i][0][3])

    # attributes name info
    new_class.attributes_coordinates = shapes_dictionary[i][1]
    new_class.attributes_lower_limit.append(shapes_dictionary[i][1][0] - 10)
    new_class.attributes_lower_limit.append(shapes_dictionary[i][1][1] - 5)
    new_class.attributes_upper_limit.append(shapes_dictionary[i][1][0] + shapes_dictionary[i][1][2])
    new_class.attributes_upper_limit.append(shapes_dictionary[i][1][1]+ shapes_dictionary[i][1][3])

    # methods name info
    new_class.methods_coordinates = shapes_dictionary[i][2]
    new_class.methods_lower_limit.append(shapes_dictionary[i][2][0] - 10)
    new_class.methods_lower_limit.append(shapes_dictionary[i][2][1] - 5)
    new_class.methods_upper_limit.append(shapes_dictionary[i][2][0] + shapes_dictionary[i][2][2])
    new_class.methods_upper_limit.append(shapes_dictionary[i][2][1]+ shapes_dictionary[i][2][3])

    classes_list.append(new_class)

parent_class = ""

for object in classes_list:
    object.is_parent(relations)
    data_type = object.data_type_matching(ocr_dictionary)
    if (image_type == "computer"):
        object.matching(ocr_dictionary, data_type)
    elif (image_type == "hand written"): 
        object.matching_hand_written(ocr_dictionary, data_type)
    object.show_info()
    if (object.isParent):
        parent_class = object.name


# write classes
class_creator.write_python_code(classes_list, parent_class)
class_creator.write_cpp_code(classes_list, parent_class)

# draw classes 
draw.draw_diagram(classes_list,ocr_dictionary,"drawings_output/output.png")

# create csv file to open using draw.io 
draw.create_csv(classes_list,parent_class)

#open draw.io then from Arrange> Insert> Advanced > CSV then copy the text in draw_csv file 
url = 'https://app.diagrams.net/'
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
#webbrowser.get('chrome').open(url)

cv2.waitKey(0)
cv2.destroyAllWindows()

