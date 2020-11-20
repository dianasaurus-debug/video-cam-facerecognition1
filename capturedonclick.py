import sys
import dlib
import cv2
import os
img_counter = 0
detector = dlib.get_frontal_face_detector()
cam = cv2.VideoCapture(0)
# For each person, enter one numeric face id
face_id = input('\n enter dataset name end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
newpath = r'D:\\image_processing\\finalproject\\dataset\\{}\\'.format(face_id) 
if not os.path.exists(newpath):
    os.makedirs(newpath)
color_green = (0,255,0)
line_width = 3
while True:
    key = cv2.waitKey(1)
    ret_val, img = cam.read()
    rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dets = detector(rgb_image)

    for det in dets:
        cv2.rectangle(img,(det.left(), det.top()), (det.right(), det.bottom()), color_green, line_width)
    cv2.imshow('my webcam', img)
    if key == 27:
        break  # esc untuk menutup
    elif key == 32:
        # space untuk mengcapture
        cv2.imshow("Capturing", img)
        img_ = cv2.resize(img[det.top():det.bottom(), det.left():det.right()],(64,64))
        cv2.imwrite(newpath + str(face_id) + "." + str(img_counter) + ".jpg", img_)
        img_name = str(face_id) + "." + str(img_counter) + ".jpg"
        cv2.waitKey(1650)
        print("{} disimpan!".format(img_name))
        img_counter += 1
        cv2.destroyWindow('Capturing')

