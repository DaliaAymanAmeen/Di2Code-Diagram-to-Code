import classes

def create_instanse (shapes_dictionary, classes_list):
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

