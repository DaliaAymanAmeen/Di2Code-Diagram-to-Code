import shape_detection 
import cv2
import classes 
import draw
#shape dictionary
print (shape_detection.shape_detection("test_images/doaa.png"))
shapes_dictionary, relations = shape_detection.shape_detection("test_images/doaa.png")

#ocr_dictionary = 
ocr_dictionary = {'User': [[414, 47]], '-': [[274, 105], [274, 125], [274, 146], [49, 427], [49, 447], [49, 468], [49, 488], [49, 508], [49, 689], [49, 709], [462, 446], [462, 466]], 'user_id': [[285, 98]], 'password': [[285, 118]], 'login_status': [[285, 138]], '+': [[274, 206], [274, 226], [49, 543], [49, 563], [49, 603], [49, 624], [49, 644], [49, 664], [462, 536], [462, 556]], 'verify_loginQ.': [[288, 203]], 'user_id()': [[289, 223]], 'Customer': [[170, 384]], 'customer_name': [[59, 421]], 'address': [[59, 440]], 'email': [[59, 460], [472, 459]], 'credit_card_info': [[59, 481]], 'shipping_info': [[59, 501]], 'customer_name()': [[64, 540]], 'address()': [[64, 560]], '+email()': [[49, 581]], 'bill': [[64, 601]], 'register()': [[64, 621]], 'login()': [[64, 641]], 'update_profile()': [[64, 662]], 'calculate_next_bill_amount()': [[59, 682]], 'generate_invoice_pdf_version()': [[59, 702]], 'Admin': [[595, 383]], 'admin_name': [[472, 439]], 'update_catalog()': [[476, 533]], 'email()': [[476, 554]]}

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

for object in classes_list:
    object.is_parent(relations)
    object.matching(ocr_dictionary)
    object.show_info()


#draw classes 
draw.draw_diagram(classes_list,ocr_dictionary,"test_images/output.png")


cv2.waitKey(0)
cv2.destroyAllWindows()

