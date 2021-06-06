import classes
import os

def write_python_code(class_list, parent):
    # python code
    class_list.sort(key = lambda x:x.isParent, reverse = True)
    child = False
    f = open("python_code.py", "w") 
    for object in class_list:
        f = open("python_code.py", "a")
        if (object.name == parent):
            child = False
        else:
            child = True
        bad_chars= [';','!',"*", "?", "'", ",", "‘", ":"]
        for i in bad_chars :
            object.name = object.name.replace(i, '')
        
        if child:
            f.write("class " + object.name + "(" + parent +")" ":\n")
        else:
            f.write("class " + object.name + ":\n")
        f.write("   def __init__(self):\n")
        for attribute in object.attributes:
            if "str" in attribute:
                index = attribute.find("str")
                initial_value = '""'
                data_type_length = 3
            elif "string" in attribute:
                index = attribute.find("string")
                initial_value = ""
                data_type_length = 6
            elif "int" in attribute:
                index = attribute.find("int")
                initial_value = 0  
                data_type_length = 3
            elif "float" in attribute:
                index = attribute.find("float")
                initial_value = 0  
                data_type_length = 5

            for i in bad_chars :
                attribute = attribute.replace(i, '')

            f.write("       self." + attribute[index+data_type_length+1:] + " = " + str(initial_value) +"\n\n")

        for method in object.methods:
            if "None" in method:
                index = method.find("None")
                return_Value = "void"
                data_type_length = 4
            if "str" in method:
                index = method.find("str")
                return_Value = "string"
                data_type_length = 3
            elif "string" in method:
                index = method.find("string")
                return_Value = "string"
                data_type_length = 6
            elif "int" in method:
                index = method.find("int")
                return_Value = "int"
                data_type_length = 3
            elif "float" in method:
                index = method.find("float")
                return_Value = "float"
                data_type_length = 5

            for i in bad_chars :
                method = method.replace(i, '')

            if ("(" in method):
                last_index = method.find("(")
                f.write("   def" + method[index + data_type_length:last_index] + "(self):" + "\n" )
            else:
                f.write("   def" + method[index + data_type_length:] + "(self):" + "\n" )
        
            f.write("       # please note that the return value is " + return_Value + "\n" )
            f.write("       pass" + "\n\n" )

    f.close()
    os.startfile("python_code.py")



def write_cpp_code (class_list, parent):
    # h file
    f = open("cpp_code.h", "w")
    f.write("#pragma once\n")
    for object in class_list:
        f = open("cpp_code.h", "a")
        if (object.name == parent):
            child = False
        else:
            child = True
        bad_chars= [';','!',"*", "?", "'", ",", "‘", ":"]
        for i in bad_chars :
            object.name = object.name.replace(i, '')
        if child:
            f.write("class " + object.name + "(" + parent +")" + "\n" + "{" + "\n" + "private: \n\n" + "public:\n" )
        else:
            f.write("class " + object.name + "\n" + "{" + "\n" + "private: \n\n" + "public:\n")
        
    
    
