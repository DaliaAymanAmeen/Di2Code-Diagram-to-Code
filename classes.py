
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
        print("class name upper limit" + str(self.name_upper_limit) + "\n")
        print("class name name" + self.name + "\n")

        print("class attribute coordinate:" + str(self.attributes_coordinates) + "\n")
        print("class attribute lower limit:" + str(self.attributes_lower_limit) + "\n")
        print("class attribute upper limit" + str(self.attributes_upper_limit) + "\n") 
        print("class attributes name" + str(self.attributes) + "\n")

        print("class methods coordinate:" + str(self.methods_coordinates) + "\n")
        print("class methods lower limit:" + str(self.methods_lower_limit) + "\n")
        print("class methods upper limit" + str(self.methods_upper_limit) + "\n")
        print("class methods name" + str(self.methods) + "\n")



    def is_parent(self, relations):
        [x, y, w, h] = self.methods_coordinates
        x_co = x + (w/2)
        y_co = y + h
        if ( (relations[0][0] < x_co+100 and relations[0][0] > x_co-100) and (relations[0][1] < y_co+100 and relations[0][1] > y_co-100) ):
            self.isParent = True 

    def matching (ocr_dictionary):
        pass

       

# ne3ml function el matching (hatlef 3ala el words) w tkaren w eli haytl3 haymela akher haga fel classes b2a 

# kda m3ana object l kol class feh kol haga n loop 3alehom sawa2 fel rasm aw el text aw el classes nfsaha

# 3ayzen haga t2oli eza da parent wala la2 