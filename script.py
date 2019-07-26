import cv2
"""
img =  cv2.imread("galaxy.jpg", 0)
# 0 denotes grayscale

print(type(img))
# img is a numpy.ndarray
print(img)
print(img.shape)
print(img.ndim)
# For grayscale the dimension of numpy array is 2
"""


img =  cv2.imread("galaxy.jpg", 1)
# 1 denotes RGB

print(type(img))
# img is a numpy.ndarray
print(img)
print(img.shape)
print(img.ndim)
# For grayscale the dimension of numpy array is 3


"""
img =  cv2.imread("galaxy.jpg", -1)
# -1 means color image but it also  has an alpha channel
#  which means it has transparency capabilities

print(type(img))
# img is a numpy.ndarray
print(img)
print(img.shape)
print(img.ndim)
# For grayscale the dimension of numpy array is 1
"""

resized_img = cv2.resize(img, (int(img.shape[1]/1.5), int(img.shape[0]/1.5)))
# We'vw resized the image, now we'll store it
cv2.imwrite("Galaxy_resized.jpg", resized_img)

cv2.imshow("Galaxy", resized_img)
# Galaxy is the name to the window
cv2.waitKey(0)
# 0 means that it will get closed when we press any key
# Any other number would mean it would wait for that many milliseconds before  getting closed by itself.
cv2.destroyAllWindows()
