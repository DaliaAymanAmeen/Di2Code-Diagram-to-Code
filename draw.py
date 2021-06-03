import shape_detection 
import cv2
import classes 

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
