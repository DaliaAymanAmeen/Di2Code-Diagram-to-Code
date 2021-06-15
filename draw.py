import shape_detection 
import cv2
import classes 
import csv
import os
import numpy as np
bad_chars= [';','!',"*", "?", "'", ",", "‘", ":", ".",'`']
        
def draw_diagram(classes_list,ocr_dictionary,output_image):
    img = cv2.imread("test_images/white.jpg")
    #img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    x=0
    y=0
    #**********************************Drawing Classes****************************
    for object in classes_list:
        [x1,y1,w1,h1]=object.name_coordinates
        [x2,y2,w2,h2]=object.attributes_coordinates
        [x3,y3,w3,h3]=object.methods_coordinates
        if(object.isParent):
            font_color=(0,0,255)
            font_size=5
            x,y=[x3+w3/2,y3+h3]
        else:
            font_color=(255,0,0)
            font_size=3

        w2=w1
        w3=w1
        img=cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),font_color ,font_size)
        x2=x1
        y2=y1+h1
        img=cv2.rectangle(img,(x2,y2),(x2+w2,y2+h2),font_color ,font_size)
        x3=x2
        y3=y2+h2
        img=cv2.rectangle(img,(x3,y3),(x3+w3,y3+h3),font_color ,font_size)
    #p1=(x,y)
    #p2=(x-50,y+50)
    #p3=(x+50,y+50)
    triangle = np.array([[x,y],[x-20,y+20],[x+20,y+20]], np.int32)
    triangleImage =cv2.polylines(img, [triangle], True, (0,0,255), thickness=2)
    #cv2.line(img, p1, p2, (0, 255, 0), 3)
    #cv2.line(img, p2, p3, (0, 255, 0), 3)
    #cv2.line(img, p1, p3, (0, 255, 0), 3)
    start_point=(int(x),int(y+20))
    for object in classes_list:
        if(not object.isParent):
            [x1,y1,w1,h1]=object.name_coordinates
            x_end,y_end=int(x1+w1/2),int(y1)
            end_point=(x_end,y_end)
            image = cv2.line(img, start_point, end_point, (0,0,255), 2)
        

   #*********************Printing Words************************************ 
    for word, coordinates_list in ocr_dictionary.items():
                for coordinates in coordinates_list:
                    x=coordinates[0]
                    y=coordinates[1]
                    #Editing the word before printing
                    for i in bad_chars :
                        word = word.replace(i, '')

                    if "ink" in word:
                        word = word.replace("ink", "int")
                    if  ")Nene" in word:
                        word = word.replace(")Nene", "None")
                    if  "-None" in word:
                        word = word.replace("-None", "None")

                    cv2.putText(img, word, (x, y+15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    cv2.imshow("out", img)    

    cv2.imwrite(output_image,img)


def create_csv(class_list,parent):
    sperator="-----------------------------------"
    users=[["ClassName","seperator1","Attributes","seperator2","Methods","Parent"]]
    keys=[["ClassName","seperator1","Attributes","seperator2","Methods","Parent"]]

    for object in class_list:

        class_name=str(object.name)
        attr=(object.attributes)
        for word ,k in zip(attr, range(len(attr))):
            for i in bad_chars :
                word = word.replace(i, '')
            if "ink" in word:
                word = word.replace("ink", "int")
            if  ")Nene" in word:
                word = word.replace(")Nene", "None")
            if  "-None" in word:
                word = word.replace("-None", "None")
            attr[k]=word
        meth=(object.methods)

        for word ,k in zip(meth, range(len(meth))):
            for i in bad_chars :
                word = word.replace(i, '')
            if "ink" in word:
                word = word.replace("ink", "int")
            if  ")Nene" in word:
                word = word.replace(")Nene", "None")
            if  "-None" in word:
                word = word.replace("-None", "None")
            meth[k]=word
        class_attributes = ' '.join([str(elem) for elem in attr])
        class_methods= ' '.join([str(elem) for elem in meth])
        
        if(object.isParent):
            user=[class_name,sperator,class_attributes,sperator,class_methods,'']
        else:
            user=[class_name,sperator,class_attributes,sperator,class_methods,parent]
        users.append(user)

    with open("draw_io_important_file.txt") as f:
        with open("drawings_output/draw_csv.csv", "w") as f1:
            for line in f:
                f1.write(line)
            #f1.write(keys)
        
    with open ("drawings_output/draw_csv.csv","a+",newline='') as draw:

        writer=csv.writer(draw)
        #writer.writerow(keys)
        writer.writerows(users)
    os.startfile("drawings_output\draw_csv.csv")
