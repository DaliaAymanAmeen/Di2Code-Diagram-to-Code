import collections
from collections import defaultdict

class Classes:
    """
    A class used to represent each class detected in the UML

    ...

    Attributes
    ----------

    self.isParent : bool

    self.name_coordinates : list
        The coordinates of the detected class name rectangles (x, y, w, h) 

    self.name_lower_limit : list
        The upper left point of the detected class name rectangles (x, y)

    self.name_upper_limit : list
        The lower right point of the detected class name rectangles (x+w, y+h)

    self.name : str
        The class name detected using OCR

    self.attributes_coordinates : list
        The coordinates of the detected attributes rectangles (x, y, w, h) 

    self.attributes_lower_limit : list
        The upper left point of the detected attributes rectangles (x, y)

    self.attributes_upper_limit : list
        The lower right point of the detected attributes rectangles (x+w, y+h)

    self.attributes : list
        The attributes detected using OCR after concatenating each attribute name
        with its data type using (matching function)

    self.methods_coordinates : list
        The coordinates of the detected methods rectangles (x, y, w, h) 

    self.methods_lower_limit : list
        The upper left point of the detected methods rectangles (x, y)

    self.methods_upper_limit : list
        The lower right point of the detected methods rectangles (x+w, y+h)

    self.methods : list
        The methods detected using OCR after concatenating each method name
        with its data type using (matching function)


    Methods
    -------
    show_info()
        Function to print the object (class) attributes 
    
    is_parent(relations)
        Function to detect whether this object (class) is a parent class or not

    data_type_matching(self, ocr_dictionary)
        Function to separate the data type from the variable name or the function name 
    
    matching (ocr_dictionary, data_type)
        Function to match each detected word that detected from OCR, and the data type with its corresponding place in the class
            (class name or attributes or methods

    matching_hand_written (ocr_dictionary, data_type)
        Function to match each detected word that detected from OCR, and the data type with its corresponding place in the class
            (class name or attributes or methods)
    """
    def __init__(self): 
        
        self.isParent = False

        self.name_coordinates = []
        self.name_lower_limit = []
        self.name_upper_limit = []
        self.name = ""

        self.attributes_coordinates = []
        self.attributes_lower_limit = []
        self.attributes_upper_limit = []
        self.attributes = []

        self.methods_coordinates = []
        self.methods_lower_limit = []
        self.methods_upper_limit = []
        self.methods = []
    
    def show_info(self):
        """Function to print the object (class) attributes 

        """
        print("is parent:" + str(self.isParent) + "\n") 

        print("class name coordinate:" + str(self.name_coordinates) + "\n")
        print("class name lower limit:" + str(self.name_lower_limit) + "\n")
        print("class name upper limit:" + str(self.name_upper_limit) + "\n")
        print("class name " + self.name + "\n")

        print("class attribute coordinate:" + str(self.attributes_coordinates) + "\n")
        print("class attribute lower limit:" + str(self.attributes_lower_limit) + "\n")
        print("class attribute upper limit:" + str(self.attributes_upper_limit) + "\n") 
        print("class attributes " + str(self.attributes) + "\n")

        print("class methods coordinate:" + str(self.methods_coordinates) + "\n")
        print("class methods lower limit:" + str(self.methods_lower_limit) + "\n")
        print("class methods upper limit:" + str(self.methods_upper_limit) + "\n")
        print("class methods" + str(self.methods) + "\n")



    def is_parent(self, relations):
        """Function to detect whether this object (class) is a parent class or not

        Parameters
        ----------
        relations : list
            The list that contains the detected triangales cooridinates (which indicate the relations)
        """
        for relation in relations:
            [x, y, w, h] = self.methods_coordinates
            x_co = x + (w/2)
            y_co = y + h
            if ( (relation[0] < x_co + 50 and relation[0] > x_co - 50) and (relation[1] < y_co + 75 and relation[1] > y_co - 75) ):
                self.isParent = True 


    def data_type_matching(self, ocr_dictionary):
        """Function to separate the data type from the variable name or the function name 

        Parameters
        ----------
        ocr_dictionary : dict
            dict {str: list} the detected word and its associated coordinates

        Returns
        -------
        data_type 
            dict {str: list} the data type and its associated coordinates
        """
        data_type = {}
        data_type_list = ['int', 'string', 'float', 'None', 'str', "-None", "):Nene", "ink"]
        for word, coordinates_list in ocr_dictionary.items():
            if (word in data_type_list):
                data_type[word] = (coordinates_list)
        return data_type


    def matching (self, ocr_dictionary, data_type):
        """Function to match each detected word that detected from OCR, and the data type with its corresponding place in the class
            (class name or attributes or methods)

        Parameters
        ----------
        ocr_dictionary : dict
            dict {str: list} the detected word and its associated coordinates

        data_type : dict
            dict {str: list} the data type and its associated coordinates

        """
        
        # first we ignore data type words
        data_type_list = ['int', 'string', 'float', 'None', 'str']
        for word, coordinates_list in ocr_dictionary.items():
            if (word in data_type_list):
                continue
            # second we ignore some symbols
            if (word == ":"):
                continue
            # finally we store classes names & attributes & methods 
            for coordinates in coordinates_list:
                #concatinate betrwee word and datatype
                for data_type_word, data_type_coordinates_list in data_type.items():
                    for data_type_coordinates in data_type_coordinates_list:
                        if (data_type_coordinates[1] <= coordinates[1]+5 and data_type_coordinates[1] >= coordinates[1]-5 and data_type_coordinates[0] <= coordinates[0]+100 and data_type_coordinates[0] >= coordinates[0]-100):
                            word = data_type_word + " " + word            
                [x, y] = coordinates
                if ((x >= self.name_lower_limit[0] and x <= self.name_upper_limit[0]) and (y >= self.name_lower_limit[1] and y <= self.name_upper_limit[1])):
                    self.name = word
                elif ((x >= self.attributes_lower_limit[0] and x <= self.attributes_upper_limit[0]) and (y >= self.attributes_lower_limit[1] and y <= self.attributes_upper_limit[1])):
                    self.attributes.append(word)
                elif ((x >= self.methods_lower_limit[0] and x <= self.methods_upper_limit[0]) and (y >= self.methods_lower_limit[1] and y <= self.methods_upper_limit[1])):
                    self.methods.append(word)

      
    def matching_hand_written (self, ocr_dictionary, data_type):
        """Function to match each detected word that detected from OCR, and the data type with its corresponding place in the class
            (class name or attributes or methods)
            
        Parameters
        ----------
        ocr_dictionary : dict
            dict {str: list} the detected word and its associated coordinates

        data_type : dict
            dict {str: list} the data type and its associated coordinates

        """
        #first we ignore data type words
        data_type_list = ['int', 'string', 'float', 'None', 'str', "-None", "):Nene", "ink"]
        for word, coordinates_list in ocr_dictionary.items():
            if (word in data_type_list):
                continue
            # second we ignore some symbols
            if (word == ":" or word == "«" or word == "|" or word == "="):
                continue
            # finally we store classes names & attributes & methods 
            for coordinates in coordinates_list:
                #concatinate betrwee word and datatype
                for data_type_word, data_type_coordinates_list in data_type.items():
                    for data_type_coordinates in data_type_coordinates_list:
                        if (data_type_coordinates[1] <= coordinates[1]+7 and data_type_coordinates[1] >= coordinates[1]-7 and data_type_coordinates[0] <= coordinates[0]+200 and data_type_coordinates[0] >= coordinates[0]-200):
                            word = data_type_word + " " + word            
                [x, y] = coordinates
                if ((x >= self.name_lower_limit[0] and x <= self.name_upper_limit[0]) and (y >= self.name_lower_limit[1] and y <= self.name_upper_limit[1])):
                    self.name = word
                elif ((x >= self.attributes_lower_limit[0] and x <= self.attributes_upper_limit[0]) and (y >= self.attributes_lower_limit[1] and y <= self.attributes_upper_limit[1]-10)):
                    self.attributes.append(word)
                elif ((x >= self.methods_lower_limit[0] and x <= self.methods_upper_limit[0]) and (y >= self.methods_lower_limit[1]-10 and y <= self.methods_upper_limit[1])):
                    self.methods.append(word)


