"""
We're are going to create a motion_detector which detects moving objects and highlights it in a rectangle
in real time through our camera.
For, it to work more accurately our first frame should be a static background frame
We'll also record the time when a moving object comes into the frame and goes out of it...

We'll store the timings in a pandas dataframe
"""
import cv2
from datetime import datetime as dt
import pandas as pd

# Storing the first frame of the video i.e a numpy array in a variable, we prefer the frame to be static
first_frame = None # We'll store it later in the while loop

status_list = [None, None] # Consist of 0 and 1, 0 represents no object present and 1 represents object present
# None is added just to prevent the IndexError
time_list = []
# Dataframe initialization
df = pd.DataFrame(columns = ['Entry', 'Exit'])

video = cv2.VideoCapture(0)

while True:
    # the loop helps us to display a series of frames as captured by the camera.
    check, frame  = video.read()

    status = 0 #First frame is considered to be static and hence 0
    # We'll use status to update status_list for each frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # we can also display the gray image

    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    """We blur the image so as to smooth it as it removes the noise and thus increasing the
    accuracy in calculation of the diffrence between the images.
    2nd parameter is the width and the height of the Gaussian Kernel which is +ve and odd,
    basically the parameters of blurness.
    the last parameter 0 is the Standard Deviation"""


    if first_frame is None:
        first_frame = gray
        continue  # When the first frame is captured we don't want to execute the rest of the code for this frame


    """Now we can apply the delta frame, that means we can calculate the difference
    between the first frame and the current frame"""

    delta_frame = cv2.absdiff(first_frame, gray)

    """Now applying threshold and obtaining its frame.
    30 (thresh)-> the threshold value for each array element of the delta_frame
    255 (maxval)-> the color we want to impart it to display in the frame when it crosses the threshold,
    It is the maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types.
    THRESH_BINARY -> it's a function which checks for thresh value and equates it maxval on crossing it
    otherwise 0.""
    cv2.threshold returns a tuple in which the first item is the thresh
    and the second item is the required frame and hence [1].
    The first item is required for other methods which are used other than THRESH_BINARY"""

    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]


    """Now to smooth the white area of threshold frame we use cv2.dilate()
    The first parameter is the original image,kernel is the matrix with which image is
    convolved and third parameter is the number of iterations,
    which will determine how much you want to dilate a given image."""

    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

    """Now we'll detect contours, for that we've two two methods
    - find contours method -> here we'll find them and store them in a tuple,
      finding contours is like finding white object from black background
    - draw contours method -> here we'll draw them"""

    cnts, heirarchy = cv2.findContours(thresh_frame.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # We'll filter out the contours Now
    for contour in cnts:
        if cv2.contourArea(contour) < 3000: # Adjust the pixel accordingly to what you wanna capture
            continue
        # Now drawing the rectangle

        status = 1 # we've found a moving

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    # Here we append the status of each frame to the status_list

    status_list.append(status)

    # We lose a lot of memory in status_list as it consists of status of each and every frame
    # We require on;y the last two status' for checking
    status_list = status_list[-2: ]  # We do this for the sake of improvement in memory saving

    # If we want the status_list to be preserved we can create a copy of it or save it to another
    # list before this step

    # Now we need to note time when an object either enters or exit the frame
    if status_list[-1]==1  and  status_list[-2]==0:
        time_list.append(dt.now())
    if status_list[-1]==0  and  status_list[-2]==1:
        time_list.append(dt.now())


    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)

    # print(gray)
    # print(delta_frame)

    if key == ord('q'):  # q for quit...lol
        if status == 1:
            time_list.append(dt.now()) #When the object has not exited the frame before pressing 'q',
            # then that time is the exit time for the object
        break

# print(status_list)
# print(time_list)

# Now appending the DataFrame, remember the pandas append is not inplace
for i in range(0, len(time_list), 2):
    #Taking 2 steps at a time
    df = df.append({"Entry": time_list[i], "Exit" : time_list[i+1]},
                    ignore_index = True)

# print(df)
df.to_csv("Times.csv")
"""We'll use this file to plot a time graph for the object , where we display the entry and exit time
of the object in our frame...
The code for this plot is written in time_plotting.py"""


video.release()  # releases the camera...

cv2.destroyAllWindows()
