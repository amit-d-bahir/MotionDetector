import cv2
import os
import glob2


def load_img_from_a_directory(filenames):
    imgs = []

    for filename in filenames:
        img = cv2.imread(filename)  # default value is 1, so it will be rgb
        resized_img = cv2.resize(img, (100, 100))
        if img is not None:
            imgs.append(resized_img)
            cv2.imshow(filename, resized_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    return imgs

filenames = glob2.glob(os.path.join(os.getcwd(), '*.jpg'))
load_img_from_a_directory(filenames)
# print(os.getcwd())
# print(filenames)
