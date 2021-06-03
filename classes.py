import collections

class Classes:
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
        for relation in relations:
            [x, y, w, h] = self.methods_coordinates
            x_co = x + (w/2)
            y_co = y + h
            if ( (relation[0] < x_co+100 and relation[0] > x_co-100) and (relation[1] < y_co+100 and relation[1] > y_co-100) ):
                self.isParent = True 

    def matching (self, ocr_dictionary):
        for word, coordinates_list in ocr_dictionary.items():
            for coordinates in coordinates_list:
                [x, y] = coordinates
                if ((x >= self.name_lower_limit[0] and x <= self.name_upper_limit[0]) and (y >= self.name_lower_limit[1] and y <= self.name_upper_limit[1])):
                    self.name = word
                elif ((x >= self.attributes_lower_limit[0] and x <= self.attributes_upper_limit[0]) and (y >= self.attributes_lower_limit[1] and y <= self.attributes_upper_limit[1])):
                    self.attributes.append(word)
                elif ((x >= self.methods_lower_limit[0] and x <= self.methods_upper_limit[0]) and (y >= self.methods_lower_limit[1] and y <= self.methods_upper_limit[1])):
                    self.methods.append(word)


