import shape_detection 
import cv2
import classes 
import csv
import os
##Habal doaa
# rasm rectangles

def draw_diagram(classes_list,ocr_dictionary,output_image):
    img = cv2.imread("test_images/white.jpg")
    #img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    for object in classes_list:
        [x1,y1,w1,h1]=object.name_coordinates
        [x2,y2,w2,h2]=object.attributes_coordinates
        [x3,y3,w3,h3]=object.methods_coordinates
        if(object.isParent):
            font_color=(0,0,255)
            font_size=5
        else:
            font_color=(255,0,0)
            font_size=3
        img=cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),font_color ,font_size)
        img=cv2.rectangle(img,(x2,y2),(x2+w2,y2+h2),font_color ,font_size)
        img=cv2.rectangle(img,(x3,y3),(x3+w3,y3+h3),font_color ,font_size)


    # rasm el kalam
    for word, coordinates_list in ocr_dictionary.items():
                for coordinates in coordinates_list:
                    x=coordinates[0]
                    y=coordinates[1]
                    cv2.putText(img, word, (x, y+10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    cv2.imshow("out", img)    

    cv2.imwrite(output_image,img)


def create_csv(class_list,parent):
    sperator="-----------------------------------"
    users=[["ClassName","seperator1","Attributes","seperator2","Methods","Parent"]]
    keys=[["ClassName","seperator1","Attributes","seperator2","Methods","Parent"]]

    for object in class_list:

        class_name=str(object.name)
        attr=(object.attributes)
        meth=(object.methods)
        class_attributes = ' '.join([str(elem) for elem in attr])
        class_methods= ' '.join([str(elem) for elem in meth])
        
        if(object.isParent):
            user=[class_name,sperator,class_attributes,sperator,class_methods,'']
        else:
            user=[class_name,sperator,class_attributes,sperator,class_methods,parent]
        users.append(user)

    with open("draw_io_important_file.txt") as f:
        with open("draw_csv.csv", "w") as f1:
            for line in f:
                f1.write(line)
            #f1.write(keys)
        
    with open ("draw_csv.csv","a+",newline='') as draw:

        writer=csv.writer(draw)
        #writer.writerow(keys)
        writer.writerows(users)
    os.startfile("draw_csv.csv")
