import shape_detection 
import cv2
import classes 

<<<<<<< Updated upstream

print (shape_detection.shape_detection("test_images/test_handwritten (2).jpeg"))

=======
print (shape_detection.shape_detection("test_images/test_handwritten.jpeg"))
class_dictionary, relations = shape_detection.shape_detection("test_images/test_handwritten.jpeg")
#ocr_dictionary = 
>>>>>>> Stashed changes


# to create instance for each class 
classes_list = []
for i in range (len(class_dictionary)):
    new_class = classes.Classes()
    # class name info
    new_class.name_coordinates =  class_dictionary[i][0]
    new_class.name_lower_limit.append(class_dictionary[i][0][0] - 10)
    new_class.name_lower_limit.append(class_dictionary[i][0][1] - 5)
    new_class.name_upper_limit.append(class_dictionary[i][0][0] + class_dictionary[i][0][2])
    new_class.name_upper_limit.append(class_dictionary[i][0][1]+ class_dictionary[i][0][3])

    # attributes name info
    new_class.attributes_coordinates = class_dictionary[i][1]
    new_class.attributes_lower_limit.append(class_dictionary[i][1][0] - 10)
    new_class.attributes_lower_limit.append(class_dictionary[i][1][1] - 5)
    new_class.attributes_upper_limit.append(class_dictionary[i][1][0] + class_dictionary[i][1][2])
    new_class.attributes_upper_limit.append(class_dictionary[i][1][1]+ class_dictionary[i][1][3])

    # methods name info
    new_class.methods_coordinates = class_dictionary[i][2]
    new_class.methods_lower_limit.append(class_dictionary[i][2][0] - 10)
    new_class.methods_lower_limit.append(class_dictionary[i][2][1] - 5)
    new_class.methods_upper_limit.append(class_dictionary[i][2][0] + class_dictionary[i][2][2])
    new_class.methods_upper_limit.append(class_dictionary[i][2][1]+ class_dictionary[i][2][3])

    classes_list.append(new_class)


#print (classes_list)
for object in classes_list:
    object.is_parent(relations)
    object.show_info()
    
cv2.waitKey(0)
cv2.destroyAllWindows()

