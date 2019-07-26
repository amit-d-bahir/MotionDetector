import cv2
import os


face_cascade = cv2.CascadeClassifier(os.path.join(os.getcwd(), 'opencv-master/data/haarcascades/haarcascade_frontalface_default.xml'))
# This creates a CascadeClassifier object

# Now we'll use this object to search for face in our image
# Now we'll load the image in python

img = cv2.imread("faces.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


"""
detectMultiScale searches the CascadeClassifier object in our image acoording to the xml file
and it returns the coordinates of the face in our image
i.e it returns the pixel row, pixel column, width and the height
"""
faces = face_cascade.detectMultiScale(gray_img,
scaleFactor = 1.1,
minNeighbors =3)

"""
The scaling Factor reduces the size by 5% and increases the chance of matching size with model for detection
Know more about it here:- http://answers.opencv.org/question/10654/how-does-the-parameter-scalefactor-in-detectmultiscale-affect-face-detection/?answer=10703#post-id-10703

minNeighbors tells python how many neighbors to search around the window
"""

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y),(x+w, y+h), (100,180,0), 3)
    """
    the 2nd and the 3rd parameter are the coordinates of the top-left and bottom-right corner of the rectangle
    the 4th parameter defines the color of the rectangle in bgr format
    the last parameter gives the width of the rectangle
    """

print(faces)
print(type(faces))


# Suppose the image resolution is bigger than the screen, than we need to resize the image
resized_img = cv2.resize(img, (int(img.shape[1] * 2), int(img.shape[0] *  2)))
cv2.imshow("img_with_face_detector", resized_img)
# cv2.imshow("img_with_face_detector", img)
# cv2.imshow("gray",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
