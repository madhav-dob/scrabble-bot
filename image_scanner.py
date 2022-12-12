from PIL import Image, ImageDraw
from pytesseract import pytesseract
from pytesseract import Output
import numpy as np
import cv2
import math
path_to_tesseract =r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image2 = Image.open("img100.png")
test_image = image2.convert("RGB")


w, h = 190, 190

def text_extractor(img):
    x1= 35
    x2= 190
    y1= 35
    y2 = 190
    k = 1
    custom_config = r' -- oem 3 -- psm 6'
    for i in range(15):
        for j in range(15):
            #print("x1-" ,x1, 'y1-',y1 ,'x2-',x2,'y2-',y2)
            img1 = img.crop((x1,y1,x2,y2))
            pytesseract.tesseract_cmd = path_to_tesseract
            text = pytesseract.image_to_data(img1,output_type= Output.DICT,config= custom_config)
            #print(k, ':' ,text[:-1])


            x1 += 177
            x2 += 177
            k+= 1
        x1 = 35
        y1 += 177
        x2 = 190
        y2 += 177
            #img1.rectangle(shape, fill ="#800080", outline ="green")
#text_extractor(test_image)

def set_image_dpi(im):

    length_x, width_y = im.size

    factor = min(1, float(1024.0 / length_x))

    size = int(factor * length_x), int(factor * width_y)

    im_resized = im.resize(size, Image.ANTIALIAS)

    kernel = np.ones((5,5),np.uint8)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

    erosion = cv2.erode(im_resized,element)

    # return cv2.fastNlMeansDenoisingColored(im_resized, None, 10, 10, 7, 15)

    # temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    #
    # temp_filename = temp_file.name
    #
    # im_resized.save(temp_filename, dpi=(300, 300))
    #
    return erosion


image4 = Image.open("img98.png")
image4.show()
# b = set_image_dpi(image4)
# # b.show()
img8 = cv2.imread('img98.png',0)
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

erosion = cv2.erode(img8, element)
kernel = np.ones((5,5),np.uint8)
# erosion = cv2.erode(img8,kernel,iterations=1)
custom_config = r' -- oem 3 -- psm 6'
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(erosion)
print( ':', text)
print('done')