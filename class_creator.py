import classes
import os

def data_type_filter (word):
    flag_str = False
    if "str" in word:
        index = word.find("str")
        initial_value = '""'
        return_Value = "string"
        data_type_length = 3
        flag_str = True    
    elif "string" in word:
        index = word.find("string")
        initial_value = ""
        return_Value = "string"
        data_type_length = 6
        flag_str = False 
    elif "int" in word:
        index = word.find("int")
        initial_value = 0  
        return_Value = "int"
        data_type_length = 3
        flag_str = False 
    elif "float" in word:
        index = word.find("float")
        initial_value = 0  
        return_Value = "float"
        data_type_length = 5  
        flag_str = False  
    elif "None" in word:
        index = word.find("None")
        initial_value = ""
        return_Value = "void"
        data_type_length = 4
        flag_str = False 

    if (flag_str):
        data_type = "string"
    else:
        data_type = word [index:data_type_length]
    variable = word [index+data_type_length+1:]

    return index, initial_value, return_Value, data_type_length, data_type, variable


def write_python_code(class_list, parent):
    # python code
    class_list.sort(key = lambda x:x.isParent, reverse = True)
    child = False
    f = open("generated code/python_code.py", "w") 
    for object in class_list:
        f = open("generated code/python_code.py", "a")
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
            index, initial_value, return_Value, data_type_length, data_type, variable = data_type_filter (attribute)

            for i in bad_chars :
                variable = variable.replace(i, '')

            f.write("       self." + variable + " = " + str(initial_value) +"\n")
        f.write("\n")

        for method in object.methods:
            index, initial_value, return_Value, data_type_length, data_type, variable = data_type_filter (method)       

            for i in bad_chars :
                variable = variable.replace(i, '')

            if ("(" in method):
                last_index = method.find("(")
                f.write("   def" + method[index + data_type_length:last_index] + "(self):" + "\n" )
            else:
                f.write("   def" + method[index + data_type_length:] + "(self):" + "\n" )
        
            f.write("       # please note that the return value is " + return_Value + "\n" )
            f.write("       pass" + "\n\n" )

    f.close()
    os.startfile("generated code\python_code.py")



def write_cpp_code (class_list, parent):
    # h file
    f = open("generated code/cpp_code.h", "w")
    f.write("#pragma once\n#include <string>\nusing namespace std;\n\n")
    for object in class_list:
        f = open("generated code/cpp_code.h", "a")
        if (object.name == parent):
            child = False
        else:
            child = True
        bad_chars= [';','!',"*", "?", "'", ",", "‘", ":"]
        for i in bad_chars :
            object.name = object.name.replace(i, '')
        if child:
            f.write("class " + object.name + " : public " + parent  + "\n" + "{" + "\n" + "private: \n" + " //write your private attributes here" + "\n" + "public:\n" )
        else:
            f.write("class " + object.name + "\n" + "{" + "\n" + "private: \n" + "  //write your private attributes here" + "\n" + "public:\n")

        for attribute in object.attributes:
            index, initial_value, return_value, data_type_length, data_type, variable = data_type_filter (attribute)

            for i in bad_chars :
                variable = variable.replace(i, '')
                data_type = data_type.replace(i, '')

            f.write("   " + data_type + " " + variable + " = " + str(initial_value) +";\n")
        f.write("\n")

        for method in object.methods:
            index, initial_value, return_value, data_type_length, data_type, variable = data_type_filter (method)

            for i in bad_chars :
                variable = variable.replace(i, '')
                data_type = data_type.replace(i, '')
            
            if ("(" in method):
                last_index = method.find("(")
                f.write("   " + return_value + " " + method[index + data_type_length:last_index] + "()" +";\n")
            else:
                f.write("   " + return_value + " " + method[index + data_type_length] + "()" +";\n")         

        #constructor & destructor
        f.write("   " + object.name + "();\n")
        f.write("   ~" + object.name + "();\n")
        f.write("};\n\n\n")
    f.close()
    os.startfile("generated code\cpp_code.h")


    # cpp file
    f = open("generated code/cpp_code.cpp", "w")
    f.write('#include "cpp_code.h"\n\n')
    for object in class_list:
        f = open("generated code/cpp_code.cpp", "a")

        for method in object.methods:
            index, initial_value, return_value, data_type_length, data_type, variable = data_type_filter (method)

            for i in bad_chars :
                variable = variable.replace(i, '')
                data_type = data_type.replace(i, '')
            
            if ("(" in method):
                last_index = method.find("(")
                f.write(return_value + " " + object.name + "::" + method[index + data_type_length:last_index] + "()" +"\n")
                f.write("{\n    //write your funtion implementation here\n" + "    return " + str(initial_value) + ";\n" +"}\n")
            else:
                f.write(return_value + " " + method[index + data_type_length] + "()" +"\n")
                f.write("{\n    //write your funtion implementation here\n" + "    return " + str(initial_value) + ";\n" + "}\n")  
    
            #constructor & destructor
            f.write(object.name + "::" + object.name + "()\n")
            f.write("{\n    //write your constructor implementation here\n}\n")
            f.write(object.name + "::" + "~" + object.name + "()\n")   
            f.write("{\n    //write your deconstructor implementation here\n}\n")    
            f.write("\n\n")

    f.close()
    os.startfile("generated code\cpp_code.cpp")

        
    
    
